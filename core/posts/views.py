from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.http import Http404, HttpResponseRedirect
from django.db.models import F

from core.posts.models import Post, SearchStatistic
from core.posts.forms import PostForm

from core.classifier.models import Category


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Post.objects.select_objects().active()[:10]
        return context


class ParentRubricView(TemplateView):
    """For base rubric text."""
    template_name = 'posts/parent_index.html'

    def get_context_data(self, **kwargs):
        """
        Get extra context for classifier to view.
        """
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['parent'])
        context['object_list'] = Post.objects.select_objects().filter(
            rubric__parent_id=context['category'].pk).active()[:4]
        return context


class PostList(ListView):
    """
    View for list of posts by category.
    """
    paginate_by = 20
    template_name = 'posts/list.html'
    ordering = '-publish_date'

    def get_context_data(self, **kwargs):
        """
        Get extra context for classifier to view.
        """
        context = super().get_context_data(**kwargs)
        category = Category.objects.select_related('meta').filter(slug=self.kwargs['child']).first()
        if category is None:
            raise Http404
        context['category'] = category
        return context

    def get_ordering(self):
        if self.request.GET.get("order"):
            return "title"
        return self.ordering

    def get_queryset(self):
        return Post.objects.select_objects().filter(
            rubric_id=get_object_or_404(Category, slug=self.kwargs['child']).id).active().order_by(self.get_ordering())


class PostSearchView(ListView):
    paginate_by = 20
    template_name = 'posts/search.html'

    def get_queryset(self):
        if self.request.GET.get('q', ''):
            SearchStatistic.objects.create(**{"fingerprint": "fingerprint",
                                              "search_phrase": self.request.GET.get('q')})
        return Post.objects.select_objects().active().annotate(
            rank=SearchRank(F('text_search'), SearchQuery(self.request.GET.get('q', ''),
                                                          config='english'))).filter(rank__gt=0).order_by('-rank')


class PostDetail(DetailView):
    """
    Return one post from list.
    """
    model = Post
    template_name = 'posts/detail.html'


class PostFormView(FormView):
    form_class = PostForm
    template_name = "posts/form.html"

    def form_valid(self, form):
        instance = form.save()
        return HttpResponseRedirect(instance.get_absolute_url())


class SiteMap(TemplateView):
    template_name = 'sitemap.xml'

    def get_context_data(self, **kwargs):
        from core.events.models import Event
        context = super(SiteMap, self).get_context_data(**kwargs)
        context['base'] = settings.HOST + '/'
        context['urls'] = [settings.HOST + p.get_absolute_url() for p in Post.objects.select_related(
            'rubric').prefetch_related('rubric__parent').filter(status=1).exclude(rubric__slug__contains='-user')]
        context['urls'].extend([f"{settings.HOST}/{slug}/" for slug in Category.objects.filter(
            level=1, is_active=True).exclude(slug__contains='-user').values_list('slug', flat=True)])
        context['urls'].extend([f"{settings.HOST}/events/{slug}.html" for slug in Event.objects.filter(
            status=1).values_list('slug', flat=True)])
        context["urls"].extend([f"{settings.HOST}/events/", f"{settings.HOST}/news/", f"{settings.HOST}/adverts/"])
        return context

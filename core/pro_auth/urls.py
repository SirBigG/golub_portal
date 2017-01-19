from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from core.pro_auth.views import RegisterView, Login, Logout, UserEmailConfirm, UserPasswordReset, IsAuthenticate, \
    SocialRegisterView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/social/(?P<backend_name>[\w-]+)/$', SocialRegisterView.as_view(), name='social-register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^is-authenticate/$', IsAuthenticate.as_view(), name='is_authenticate'),
    url(r'^confirm/email/(?P<hash>[\w-]+).html$', UserEmailConfirm.as_view(), name='email_confirm'),
    url(r'^password/(?P<action>confirm)/email/', UserPasswordReset.as_view(), name='password-reset'),
    url(r'^password/(?P<action>check)/email/(?P<hash>[\w-]+).html$',
        UserPasswordReset.as_view(), name='password-check'),
    # Rendering index page for all urls starts with /user/<user_id>/ for personal page.
    url(r'^user/(?P<pk>\d+)/', login_required(TemplateView.as_view(template_name='personal/personal_index.html')),
        name='personal-index'),
]
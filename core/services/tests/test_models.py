from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from core.utils.tests.factories import FeedbackFactory, MetaDataFactory, CommentsFactory, PostFactory, UserFactory


class FeedbackModelTest(TestCase):

    def setUp(self):
        self.feedback = FeedbackFactory()

    def test_str_representation(self):
        self.assertEqual(str(self.feedback), 'Feedback topic')


class MetaDataTests(TestCase):

    def setUp(self):
        self.meta = MetaDataFactory()

    def test_str_representation(self):
        self.assertEqual(str(self.meta), 'title')


class CommentsTests(TestCase):
    def setUp(self):
        user = UserFactory()
        ct = ContentType.objects.get(model='post')
        post = PostFactory()
        self.comment = CommentsFactory(content_type=ct, object_id=post.pk, user=user)

    def test_str_representation(self):
        self.assertEqual(str(self.comment), 'comment text')
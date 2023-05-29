from django.test import TestCase

from blog.models import Article
from users.models import User
from django.urls import reverse

# test Article functionality : 
class ArticleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.article = Article.objects.create(
            title='Test Article',
            description='Test Description',
            body='Test Body',
            author=self.user,
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_article_ordering(self):
        articles = Article.objects.all()
        self.assertEqual(list(articles), [self.article])

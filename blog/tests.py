from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
'''
class TestIndex(SimpleTestCase):
	def test_url_code_index(self):
		response=self.client.get("/")
		self.assertEqual(response.status_code,200)
class TestPortfolio(SimpleTestCase):
	def test_url_code_portfolio(self):
		response=self.client.get("/olatide-joseph-adeniyi")
		self.assertEqual(response.status_code,200)
	def test_endpoint_url(self):
		self.assertEqual(reverse('olatide'),"/olatide-joseph-adeniyi")

class TestDatabaseClient(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.post=Post.objects.create(text="this is a test data")
	def test_data_content(self):
		txt=self.post.text
		self.assertEqual(txt,"this is a test data")

'''

class BlogTestCase(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.post=Post.objects.create(text="this is a blog test")
	def test_home_url(self):
		response=self.client.get("/")
		self.assertEqual(response.status_code,200)
	def test_home_name(self):
		response=self.client.get(reverse('index'))
		self.assertEqual(response.status_code,200)
	def test_blog_database(self):
		self.assertEqual(self.post.text,"this is a blog test")
	def test_home_template_content(self):
		response=self.client.get("/")
		self.assertTemplateUsed(response,"index.html")
	def test_home_contains(self):
		response=self.client.get("/")
		self.assertContains(response,"Creator Portfolio")
	def test_portfolio_url(self):
		response=self.client.get("/olatide-joseph-adeniyi")
		self.assertEqual(response.status_code,200)

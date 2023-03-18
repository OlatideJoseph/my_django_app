from django.test import TestCase#,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
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
		cls.user=get_user_model().objects.create(
			username='testuser',
			email='test2@email.com',
			password='secret')
		cls.post=Post.objects.create(
			author=cls.user,
			title="test title",
			text="this is a blog test"
			)
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

	def test_user_model(self):
		self.assertEqual(self.user.username,"testuser")
		self.assertEqual(self.user.email,"test2@email.com")
		self.assertEqual(self.user.password,'secret')


	def test_post_models(self):
		self.assertEqual(self.post.title,"test title")
		self.assertEqual(self.post.text,"this is a blog test")
		self.assertEqual(self.post.author,self.user)
		self.assertEqual(self.post.author.username,"testuser")
		self.assertEqual(self.post.author.id,1)
		self.assertEqual(self.post.id,1)
	def test_post_details(self):
		response=self.client.get('/post/1')
		no0_response=self.client.get('post/1000')
		self.assertEqual(no0_response.status_code,404)
		self.assertEqual(response.status_code,200)

	def test_post_createview(self):
		response=self.client.post(reverse('create-post'),
            {
            'title':'the test post',
            'text':'A new test post for the django driven development',
            'author':self.user.id
            }
			)
		self.assertEqual(response.status_code,302)
		self.assertEqual(Post.objects.last().title,"the test post")
		self.assertEqual(Post.objects.last().text,"A new test post for the django driven development")
	def test_post_updateview(self):
		response=self.client.post(reverse('edit_post',args="1"),
            {
            'title':'The edited blog post',
            'text':"the blog post content"
            }
			)
		self.assertEqual(response.status_code,302)
		self.assertEqual(Post.objects.last().title,"The edited blog post")
		self.assertEqual(Post.objects.last().text,"the blog post content")
	def test_post_deleteview(self):
		response=self.client.post(reverse('delete_post',args='1'))
		self.assertEqual(response.status_code,302)
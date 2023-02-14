from django.test import TestCase,SimpleTestCase
from django.urls import reverse

# Create your tests here.

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


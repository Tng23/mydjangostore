from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .models import Product

class HomePageTest(SimpleTestCase):

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


class ProductTests(TestCase):

    @classmethod
    def setUp(cls):
        Product.objects.create(name='product name')

    def test_text(self):
        product = Product.objects.get(id=1)
        expected_product_name = post.name
        self.assertEquals(expected_product_name, 'product name')

    def test_product_view(self):
        response = self.client.get(reverse('products'))
        self.assertEquals(response.stats_code, 200)
        self.assertContains(response, 'product name')
        self.assertTemplateUsed(response, 'product.html')

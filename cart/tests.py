from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .models import Cart

class CartTests(TestCase):

    @classmethod
    def setUp(cls):
        Cart.objects.create(name='cart name')

    def test_text(self):
        cart = Cart.objects.get(id=1)
        expected_cart_name = cart.name
        self.assertEquals(expected_cart_name, 'cart name')

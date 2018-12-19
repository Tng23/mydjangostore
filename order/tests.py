from django.test import TestCase, SimpleTestCase

class OrderHistoryTest(SimpleTestCase):

    def test_order_history_status_code(self):
        response = self.client.get('order_history')
        self.assertEquals(response.status_code, 200)

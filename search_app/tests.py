from django.test import TestCase, SimpleTestCase

class SearchPageTest(SimpleTestCase):

    def test_search_status_code(self):
        response = self.client.get('searchResult')
        self.assertEquals(response.status_code, 200)

from django.test import TestCase

# Create your tests here.

class TestProducts(TestCase):

    def test_index(self):
        response = self.client.get('/products/')
        self.assertEquals(response.status_code, 200)

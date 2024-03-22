from django.test import TestCase

# Create your tests here.

class TestProducts(TestCase):

    def test_index1(self):
        response = self.client.get('/users/login/')
        self.assertEquals(response.status_code, 200)
    def test_index2(self):
        response = self.client.get('/users/registration/')
        self.assertEquals(response.status_code, 200)
    def test_index3(self):
        response = self.client.get('/users/profile/')
        self.assertEquals(response.status_code, 302)
    def test_index4(self):
        response = self.client.get('/users/logout/')
        self.assertEquals(response.status_code, 302)

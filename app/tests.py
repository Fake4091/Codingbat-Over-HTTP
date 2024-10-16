from django.test import SimpleTestCase

# Create your tests here.


class TestNear100(SimpleTestCase):
    def test_98_near_100(self):
        response = self.client.get("/near-100/98")
        self.assertContains(response, "True")

    def test_89_near_100(self):
        response = self.client.get("/near-100/89")
        self.assertContains(response, "False")

    def test_90_near_100(self):
        response = self.client.get("/near-100/90")
        self.assertContains(response, "True")

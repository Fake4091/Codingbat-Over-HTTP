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


class TestStringSplosion(SimpleTestCase):
    def test_abc_string_splosion(self):
        response = self.client.get("/string-splosion/abc")
        self.assertContains(response, "aababc")

    def test_code_string_splosion(self):
        response = self.client.get("/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_ab_string_splosion(self):
        response = self.client.get("/string-splosion/ab")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_cat_dog(self):
        response = self.client.get("/cat-dog/catdog")
        self.assertContains(response, "True")

    def test_catcat(self):
        response = self.client.get("/cat-dog/catcat")
        self.assertContains(response, "False")

    def test_1cat1cadodog(self):
        response = self.client.get("/cat-dog/1cat1cadodog")
        self.assertContains(response, "True")

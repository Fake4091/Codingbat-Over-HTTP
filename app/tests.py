from django.test import SimpleTestCase

# Create your tests here.


class TestNear100(SimpleTestCase):
    def test_98_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/98")
        self.assertContains(response, "True")

    def test_89_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, "False")

    def test_90_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, "True")


class TestStringSplosion(SimpleTestCase):
    def test_abc_string_splosion(self):
        response = self.client.get("/warmup-2/string-splosion/abc")
        self.assertContains(response, "aababc")

    def test_code_string_splosion(self):
        response = self.client.get("/warmup-2/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_ab_string_splosion(self):
        response = self.client.get("/warmup-2/string-splosion/ab")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_cat_dog(self):
        response = self.client.get("/string-2/cat-dog/catdog")
        self.assertContains(response, "True")

    def test_catcat(self):
        response = self.client.get("/string-2/cat-dog/catcat")
        self.assertContains(response, "False")

    def test_1cat1cadodog(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_3_2_3(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3")
        self.assertContains(response, "2")

    def test_1_2_3(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3")
        self.assertContains(response, "6")

    def test_3_3_3(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response, "0")

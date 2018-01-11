from django.test import TestCase


class BasicTest(TestCase):

    def test_basic_addition(self):
        self.assertEqual(2 * 2, 5)

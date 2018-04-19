from unittest import TestCase
from src.bloom import Bloom


class TestBloom(TestCase):
    def test_object_creation(self):
        Bloom()
        Bloom(1, 2, 3)
        Bloom(1, 2, 3, 4)
        Bloom([1, 2, 3, 4])
        Bloom(1, 2, size=2, hash_functions=[lambda x: x % 2])
        Bloom(1, 2, hash_functions=[lambda x: x % 2])

    def test_equals(self):
        self.assertEqual(Bloom(), Bloom())
        self.assertEqual(Bloom(1, 2, 3), Bloom([1, 2, 3]))

    def test_membership(self):
        self.assertIn(1, Bloom(1))

    def test_not_in_empty(self):
        self.assertNotIn(1, Bloom())
        self.assertNotIn(1, Bloom([]))

    def test_add_function(self):
        a = Bloom()
        a.add(2)
        self.assertIn(2, a)

    def test_object_creation_with_list(self):
        a = Bloom([1, 2, 3])
        self.assertIn(1, a)
        self.assertIn(2, a)
        self.assertIn(3, a)

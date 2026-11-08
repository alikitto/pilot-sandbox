import unittest

from slugcheck import is_slug


class IsSlugTests(unittest.TestCase):
    def test_accepts_valid_slugs(self):
        for value in ("hello-world", "a", "abc-123"):
            with self.subTest(value=value):
                self.assertTrue(is_slug(value))

    def test_rejects_invalid_slugs(self):
        for value in ("", "-a", "a-", "a--b", "Hello", "a b", "café"):
            with self.subTest(value=value):
                self.assertFalse(is_slug(value))


if __name__ == "__main__":
    unittest.main()

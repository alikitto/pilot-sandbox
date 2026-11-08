import unittest

from slugtrunc import truncate_slug


class TruncateSlugTests(unittest.TestCase):
    def test_short_slug_is_unchanged(self):
        self.assertEqual(truncate_slug("hello-world", 20), "hello-world")

    def test_truncates_at_last_hyphen_within_limit(self):
        self.assertEqual(truncate_slug("hello-world", 10), "hello")
        self.assertEqual(truncate_slug("hello-world-foo", 12), "hello-world")

    def test_hard_cuts_when_first_word_exceeds_limit(self):
        self.assertEqual(truncate_slug("supercalifragilistic", 5), "super")

    def test_nonpositive_limit_returns_empty_string(self):
        self.assertEqual(truncate_slug("a-b", 0), "")
        self.assertEqual(truncate_slug("abc", -1), "")


if __name__ == "__main__":
    unittest.main()

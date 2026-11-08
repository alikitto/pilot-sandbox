import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_replaces_punctuation_and_spaces(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_whitespace(self):
        self.assertEqual(slugify("  A  B  "), "a-b")

    def test_replaces_runs_of_symbols(self):
        self.assertEqual(slugify("C++ & Rust"), "c-rust")

    def test_all_symbol_input_returns_empty_string(self):
        self.assertEqual(slugify("---"), "")

    def test_empty_input_returns_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_preserves_existing_hyphens_and_digits(self):
        self.assertEqual(slugify("Already-Slugged-123"), "already-slugged-123")


if __name__ == "__main__":
    unittest.main()

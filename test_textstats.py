import unittest

from textstats import word_count


class WordCountTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)

    def test_whitespace_only_string(self):
        self.assertEqual(word_count(" \t\n "), 0)

    def test_single_word(self):
        self.assertEqual(word_count("hello"), 1)

    def test_two_words(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_words_separated_by_mixed_whitespace(self):
        self.assertEqual(word_count("  a  b\tc\nd "), 4)


if __name__ == "__main__":
    unittest.main()

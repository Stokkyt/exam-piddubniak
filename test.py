import unittest
from main import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_ukrainian_word(self):
        self.assertEqual(count_vowels("книга"), 2)
        self.assertEqual(count_vowels("мова"), 2)

    def test_english_word(self):
        self.assertEqual(count_vowels("education"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("MoViE"), 3)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

if __name__ == "__main__":
    unittest.main()

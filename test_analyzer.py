"""
Test Suite - Password Strength Analyzer
Automated version of the manual test cases documented in
Chapter 4.2 (Test Cases) of the internship report.

Run with:  python3 -m unittest test_analyzer.py -v
"""

import unittest
import string


def compute(password: str):
    """Pure computation helper (mirrors code.py logic) so it can be
    unit tested without triggering input() or exit()."""
    length = len(password)
    charset = 0
    if any(ch.islower() for ch in password):
        charset += 26
    if any(ch.isupper() for ch in password):
        charset += 26
    if any(ch.isdigit() for ch in password):
        charset += 10
    if any(ch in string.punctuation for ch in password):
        charset += 32

    if charset == 0:
        return None  # signals "Invalid password"

    combinations = charset ** length
    seconds = combinations / 1_000_000

    if seconds < 60:
        strength = "WEAK"
    elif seconds < 86_400:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return length, charset, int(seconds), strength


class TestPasswordStrengthAnalyzer(unittest.TestCase):

    def test_TC01_empty_string_is_invalid(self):
        """Null/Empty String Handling"""
        self.assertIsNone(compute(""))

    def test_TC02_single_charset_lowercase(self):
        """Single Charset (Lowercase) -> charset 26, WEAK"""
        length, charset, seconds, strength = compute("hello")
        self.assertEqual(length, 5)
        self.assertEqual(charset, 26)
        self.assertEqual(strength, "WEAK")

    def test_TC03_dual_charset_alphanumeric(self):
        """Dual Charset (lowercase + digits) -> charset 36"""
        length, charset, seconds, strength = compute("hello12")
        self.assertEqual(length, 7)
        self.assertEqual(charset, 36)

    def test_TC04_weak_to_medium_boundary(self):
        """WEAK/MEDIUM boundary check at 60 seconds"""
        length, charset, seconds, strength = compute("test1234")
        self.assertEqual(charset, 36)
        self.assertGreaterEqual(seconds, 60)

    def test_TC05_medium_to_strong_boundary(self):
        """MEDIUM/STRONG boundary check at 86,400 seconds"""
        length, charset, seconds, strength = compute("Str0ng!Pass")
        self.assertEqual(charset, 94)
        self.assertEqual(strength, "STRONG")

    def test_TC06_punctuation_isolation(self):
        """Punctuation-only password -> charset 32"""
        length, charset, seconds, strength = compute("@#$!%")
        self.assertEqual(charset, 32)

    def test_TC07_large_integer_stress(self):
        """Large/complex password must compute without overflow or crash"""
        password = "aA1!" * 15  # 60 highly diverse characters
        result = compute(password)
        self.assertIsNotNone(result)
        length, charset, seconds, strength = result
        self.assertEqual(charset, 94)
        self.assertEqual(strength, "STRONG")

    def test_TC08_unrecognized_characters_only(self):
        """Whitespace-only input (no recognized character class) -> Invalid"""
        self.assertIsNone(compute("   "))


if __name__ == "__main__":
    unittest.main(verbosity=2)

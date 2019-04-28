#  Copyright (c) 2019 Benjamin Ezepue
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

"""
Test module for the Outcome class

"""

import unittest

from ood_outcome import Outcome


class TestOutcomeMethods(unittest.TestCase):
    """
    Test class for the Outcome class methods

    """

    def setUp(self):
        """
        setup function for the TestOutcomeMethods class

        """
        self.outcome = Outcome('Red', 17)

    def test_win_amount(self):
        """
        Tests that the amount returned by the win_amount method is correct

        """
        win_amount = self.outcome.win_amount(2)
        self.assertEqual(win_amount, 34)

    def test_compare_equal(self):
        """
        Tests that two Outcome objects with the same name are equal

        """
        other_outcome = Outcome('Red', 18)
        self.assertTrue(self.outcome == other_outcome)

    def test_compare_not_equal(self):
        """
        Tests that two Outcome objects that do not have the same name are unequal

        """
        other_outcome = Outcome('Black', 17)
        self.assertTrue(self.outcome != other_outcome)

    def test_hash_equal(self):
        """
        Tests that the hash values of two Outcome objects with the same name are equal

        """
        other_outcome = Outcome('Red', 18)
        self.assertTrue(hash(self.outcome) == hash(other_outcome))

    def test_string_representation(self):
        """
        Tests that the string returned by str(Outcome) has the correct format

        """
        expected_string = 'Red (17:1)'
        self.assertTrue(str(self.outcome) == expected_string)


if __name__ == '__main__':
    unittest.main()

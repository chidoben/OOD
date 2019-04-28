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
Test module for the bin class

"""

import unittest

from ood_bin import Bin
from ood_outcome import Outcome


class TestBin(unittest.TestCase):
    """
    Test class for the Bin class.
    This unit test class creates several instances of Outcome, two instances of Bin
    and establishes that Bins can be constructed from the Outcomes.

    """

    def setUp(self):
        """
        setup function for the TestBin class

        """
        self.outcome_1 = Outcome('Red', 17)
        self.outcome_2 = Outcome('00-0-1-2-3', 6)
        self.outcome_3 = Outcome('00', 35)

    def test_construct_bin_from_outcomes(self):
        """
        Tests that bins can be constructed from instances of the outcome class

        """
        bin1 = Bin({self.outcome_1, self.outcome_2, self.outcome_3})
        bin2 = Bin({self.outcome_1, Outcome('00-0-1-2-3', 6), self.outcome_3})

        self.assertEqual(bin1, bin2)


if __name__ == '__main__':
    unittest.main()

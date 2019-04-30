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

from ood_wheel import Wheel
from ood_outcome import Outcome
from ood_bin import Bin


class TestWheel(unittest.TestCase):
    """
    Test class for the Wheel class.
    This unit test class creates several instances of Outcome, two instances of Bin, and an instance of Wheel and
    establishes that Bins can be added to the Wheel.
    """

    def setUp(self):
        """
        setup function for the TestBin class

        """
        self.wheel = Wheel()
        self.outcome_1 = Outcome('Red', 17)
        self.outcome_2 = Outcome('00-0-1-2-3', 6)
        self.outcome_3 = Outcome('00', 35)
        self.bin1 = Bin({self.outcome_1, self.outcome_2, self.outcome_3})
        self.bin2 = Bin({self.outcome_1, Outcome('00-0-1-2-3', 6), self.outcome_3})

    def test_add_outcome_to_wheel_bin(self):
        """
        Tests that bins can be added to the wheel

        """
        self.wheel.add_outcome_to_wheel_bin(0, self.outcome_1)
        self.wheel.add_outcome_to_wheel_bin(0, self.outcome_2)
        self.wheel.add_outcome_to_wheel_bin(0, self.outcome_3)
        self.assertEqual(self.wheel.get_wheel_bin(0), self.bin1)

        self.wheel.add_outcome_to_wheel_bin(1, self.outcome_1)
        self.wheel.add_outcome_to_wheel_bin(1, self.outcome_3)
        self.wheel.add_outcome_to_wheel_bin(1, Outcome('00-0-1-2-3', 6))
        self.assertEqual(self.wheel.get_wheel_bin(1), self.bin2)


class TestWheelRandomChoice(unittest.TestCase):
    """
     This  unit test class tests the Wheel class by selecting “random” values from a Wheel object
     using a fixed seed value.
    """

    def setUp(self):
        """
        setup function for the TestBin class

        """
        self.wheel = Wheel()
        self.wheel.random_number_generator.seed(1)

    def test_next_wheel_bin(self):
        """
        Tests that calling the next_wheel_bin method selects a random Bin from the Wheel.

        """
        expected_random_bin = [8, 36, 4, 16, 7, 31, 28, 30, 24, 13]
        for bin_number in range(10):
            self.assertEqual(self.wheel.bins[expected_random_bin[bin_number]], self.wheel.next_wheel_bin())


if __name__ == '__main__':
    unittest.main()

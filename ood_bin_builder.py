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
The Bin Builder module.

This module contains the BinBuilder class.
"""

from ood_wheel import Wheel
from ood_outcome import Outcome


class BinBuilder:
    """
    BinBuilder creates the Outcomes for all of the 38 individual Bin on a Roulette wheel.

    """

    def __init__(self):
        """Initializes the BinBuilder.

        """
        self.wheel = Wheel()

    def build_bins(self, wheel):
        """Creates the Outcome instances and uses the addOutcome() method to place each
        Outcome in the appropriate Bin of wheel

        Parameter:
            wheel (Wheel): The Wheel with Bins that must be populated with Outcomes.

        """
        pass

    def generate_straight_bets(self):
        """

        """
        pass

    def generate_split_bets(self):
        """

        """
        pass

    def generate_street_bets(self):
        """

        """
        pass

    def generate_corner_bets(self):
        """

        """
        pass

    def generate_line_bets(self):
        """

        """
        pass

    def generate_dozen_bets(self):
        """

        """
        pass

    def generate_column_bets(self):
        """

        """
        pass

    def generate_money_bets(self):
        """

        """
        pass

    def generate_special_case_zero(self):
        """

        """
        pass

    def generate_special_case_double_zero(self):
        """

        """
        pass

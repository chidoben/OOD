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
        pass

    def build_bins(self, wheel):
        """Creates the Outcome instances and uses the addOutcome() method to place each
        Outcome in the appropriate Bin of wheel

        Parameter:
            wheel (Wheel): The Wheel with Bins that must be populated with Outcomes.

        """
        self.generate_column_bets(wheel)
        self.generate_corner_bets(wheel)
        self.generate_line_bets(wheel)
        self.generate_dozen_bets(wheel)
        self.generate_money_bets(wheel)
        self.generate_special_case_double_zero(wheel)
        self.generate_special_case_zero(wheel)
        self.generate_split_bets(wheel)
        self.generate_street_bets(wheel)
        self.generate_straight_bets(wheel)

    def generate_straight_bets(self, wheel):
        """
        Generates the straight bets outcomes and adds them to the appropriate bin of the wheel

        """
        for number in range(1, 37):
            wheel.add_outcome_to_wheel_bin(number, Outcome(str(number), 35))

    def generate_split_bets(self, wheel):
        """
        Generates the split bets outcomes and adds them to the appropriate bins of the wheel

        """
        # left-right split bets
        for row in range(12):
            # Column 1-2 split
            first_column_number = (3 * row) + 1
            wheel.add_outcome_to_wheel_bin(first_column_number, Outcome(
                "{" + "{} - {}".format(str(first_column_number), str(first_column_number + 1)) + "}", 17))
            wheel.add_outcome_to_wheel_bin(first_column_number + 1, Outcome(
                "{" + "{} - {}".format(str(first_column_number), str(first_column_number + 1)) + "}", 17))

            # column 2-3 split
            second_column_number = (3 * row) + 2
            wheel.add_outcome_to_wheel_bin(second_column_number, Outcome(
                "{" + "{} - {}".format(str(first_column_number), str(first_column_number + 1)) + "}", 17))
            wheel.add_outcome_to_wheel_bin(second_column_number + 1, Outcome(
                "{" + "{} - {}".format(str(first_column_number), str(first_column_number + 1)) + "}", 17))

        # up-down split bets
        for number in range(1, 34):
            wheel.add_outcome_to_wheel_bin(number,
                                           Outcome("{" + "{} - {}".format(str(number), str(number + 3)) + "}", 17))
            wheel.add_outcome_to_wheel_bin(number + 3,
                                           Outcome("{" + "{} - {}".format(str(number), str(number + 3)) + "}", 17))

    def generate_street_bets(self, wheel):
        """
        Generates the street bets outcomes and assigns them to the appropriate bins of the wheel

        """
        for row in range(12):
            first_column_number = (3 * row) + 1
            wheel.add_outcome_to_wheel_bin(first_column_number, Outcome(
                "{" + "{} - {} - {}".format(str(first_column_number), str(first_column_number + 1),
                                            str(first_column_number + 2)) + "}", 11))
            wheel.add_outcome_to_wheel_bin(first_column_number + 1, Outcome(
                "{" + "{} - {} - {}".format(str(first_column_number), str(first_column_number + 1),
                                            str(first_column_number + 2)) + "}", 11))
            wheel.add_outcome_to_wheel_bin(first_column_number + 2, Outcome(
                "{" + "{} - {} - {}".format(str(first_column_number), str(first_column_number + 1),
                                            str(first_column_number + 2)) + "}", 11))

    def generate_corner_bets(self, wheel):
        """
        Generates the corner bets outcomes and assigns them to the appropriate bins of the wheel

        """

        def add_outcome_to_wheel(column_number, wheel):
            """
            Helper function to add the outcome to the bins of the wheel

            """
            wheel.add_outcome_to_wheel_bin(column_number, Outcome(
                "{" + "{} - {} - {} - {}".format(str(column_number), str(column_number + 1),
                                                 str(column_number + 3), str(column_number + 4)) + "}", 8))
            wheel.add_outcome_to_wheel_bin(column_number + 1, Outcome(
                "{" + "{} - {} - {} - {}".format(str(column_number), str(column_number + 1),
                                                 str(column_number + 3), str(column_number + 4)) + "}", 8))
            wheel.add_outcome_to_wheel_bin(column_number + 3, Outcome(
                "{" + "{} - {} - {} - {}".format(str(column_number), str(column_number + 1),
                                                 str(column_number + 3), str(column_number + 4)) + "}", 8))
            wheel.add_outcome_to_wheel_bin(column_number + 4, Outcome(
                "{" + "{} - {} - {} - {}".format(str(column_number), str(column_number + 1),
                                                 str(column_number + 3), str(column_number + 4)) + "}", 8))

        for row in range(11):
            # column 1-2 corner
            first_column_number = (3 * row) + 1
            add_outcome_to_wheel(first_column_number, wheel)

            # column 2-3 corner
            second_column_number = (3 * row) + 2
            add_outcome_to_wheel(second_column_number, wheel)

    def generate_line_bets(self, wheel):
        """
        Generates the line bets outcomes and adds them to the appropriate bins of the wheel

        """

        def column_outcome(column_number):
            return Outcome("{" + "{} - {} - {} - {} - {} - {}".format(str(column_number), str(column_number + 1),
                                                                      str(column_number + 2),
                                                                      str(column_number + 3), str(column_number + 4),
                                                                      str(column_number + 5)) + "}", 5)

        for row in range(11):
            first_column_number = (3 * row) + 1
            wheel.add_outcome_to_wheel_bin(first_column_number, column_outcome(first_column_number))
            wheel.add_outcome_to_wheel_bin(first_column_number + 1, column_outcome(first_column_number))
            wheel.add_outcome_to_wheel_bin(first_column_number + 2, column_outcome(first_column_number))
            wheel.add_outcome_to_wheel_bin(first_column_number + 3, column_outcome(first_column_number))
            wheel.add_outcome_to_wheel_bin(first_column_number + 4, column_outcome(first_column_number))
            wheel.add_outcome_to_wheel_bin(first_column_number + 5, column_outcome(first_column_number))

    def generate_dozen_bets(self, wheel):
        """
         Generates the dozen bets outcomes and adds them to the appropriate bins of the wheel
        """
        for dozen in range(3):
            dozen_outcome = Outcome(str(dozen + 1), 2)
            for number in range(12):
                wheel.add_outcome_to_wheel_bin((12 * dozen) + number + 1, dozen_outcome)

    def generate_column_bets(self, wheel):
        """
         Generates the column bets outcomes and adds them to the appropriate bins of the wheel
        """
        for column in range(3):
            column_outcome = Outcome(str(column + 1), 2)
            for row in range(12):
                wheel.add_outcome_to_wheel_bin((3 * row) + column + 1, column_outcome)

    def generate_money_bets(self, wheel):
        """
        Generates the money bets outcomes and adds them to the appropriate bins of the wheel

        """
        red_outcome = Outcome("Red", 1)
        black_outcome = Outcome("Black", 1)
        even_outcome = Outcome("Even", 1)
        odd_outcome = Outcome("Odd", 1)
        high_outcome = Outcome("High", 1)
        low_outcome = Outcome("Low", 1)
        for number in range(1, 37):
            if 1 <= number < 19:
                wheel.add_outcome_to_wheel_bin(number, low_outcome)
            else:
                wheel.add_outcome_to_wheel_bin(number, high_outcome)

            if number % 2 == 0:
                wheel.add_outcome_to_wheel_bin(number, even_outcome)
            else:
                wheel.add_outcome_to_wheel_bin(number, odd_outcome)

            if number in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}:
                wheel.add_outcome_to_wheel_bin(number, red_outcome)
            else:
                wheel.add_outcome_to_wheel_bin(number, black_outcome)

    def generate_special_case_zero(self, wheel):
        """
        Creates an outcome from '0' and assigns it to bin 0 of the wheel
        """
        wheel.add_outcome_to_wheel_bin(0, Outcome('0', 35))

    def generate_special_case_double_zero(self, wheel):
        """
        Creates an outcome from '00' and assigns it to bin 37 of the wheel

        """
        wheel.add_outcome_to_wheel_bin(37, Outcome('00', 35))

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
The Outcome module.

This module contains the outcome class.
The outcome class contains the name of the outcome as a String, and the odds that are
paid as an integer. We will use these objects when placing a bet and also when defining
the Roulette wheel.
"""


class Outcome:
    """
    Outcome contains a single outcome on which a bet can be placed

    Fields:
       name: Holds the name of the Outcome.
       odds: Holds the payout odds for this Outcome.

    """

    def __init__(self, name, odds):
        """Sets the instance name and odds from the parameter name and odds.

        Parameters:
            name (str): The name of this outcome.
            odds (int): The payout odds of this outcome.

        """
        self.name = name
        self.odds = odds

    def win_amount(self, amount):
        """Multiplies this Outcome's odds by the given amount The product is returned.

        Parameter:
            amount (float): amount being bet on.

        Returns:
            The result of the multiplication

        """
        return self.odds * amount

    def __eq__(self, other):
        """Compare the name attributes of self and other

        Parameter:
            other (Outcome): Another Outcome to compare against

        Returns:
            True if this name matches the other name.

        Return type:
            bool

        """
        return self.name == other.name

    def __ne__(self, other):
        """Compare the name attributes of self and other

        Parameter:
            other (Outcome): Another Outcome to compare against

        Returns:
            True if this name does not match the other name.

        Return type:
            bool

        """
        return self.name != other.name

    def __hash__(self):
        """ Hash value for this outcome.

        Returns:
            The hash value of the name, hash(self.name).

        Return type:
            int

        """
        return hash(self.name)

    def __str__(self):
        """Easy-to-read representation of this outcome

        Returns:
            String of the form 'name (odds:1)'

        Return type:
            str

        """
        return "%s (%d:1)" % (self.name, self.odds)

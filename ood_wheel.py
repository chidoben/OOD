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
The Wheel module.

This module contains the Wheel class
The wheel has two responsibilities: it is a container for the Bins
and it picks one Bin at random.
"""

from os import urandom
from random import Random
from ood_bin import Bin


class Wheel:
    """
    Wheel contains the 38 individual bins on a Roulette wheel, plus a random number generator.
    It can select a Bin at random, simulating a spin of the Roulette wheel.

    Fields:
        bins: Contains the individual Bin instances.
        rng:  A random number generator to use to select a Bin from the bins collection.
    """

    def __init__(self):
        """Creates a new wheel with 38 empty Bins.
           It will also create a new random number generator instance.

        """
        self.bins = [Bin() for _ in range(38)]
        self.random_number_generator = Random()

    def add_outcome_to_wheel_bin(self, bin_number, outcome):
        """Adds the given Outcome to the Bin with the given number.

        Parameters:
            bin_number(int) – bin number, in the range zero to 37 inclusive.
            outcome(Outcome) – The Outcome to add to this Bin
        """
        self.bins[bin_number] |= Bin({outcome})

    def next_wheel_bin(self):
        """Generates a random number between  0 and 37, and returns the randomly selected Bin.

        Returns:
            A Bin selected at random from the wheel.

        Return type:
             Bin
        """
        self.random_number_generator.seed(urandom(20))
        return self.random_number_generator.choice(self.bins)

    def get_wheel_bin(self, bin_number):
        """Returns the given Bin from the internal collection.

        Parameters:
            bin_number(int) – bin number, in the range zero to 37 inclusive.

        Returns:
            The requested Bin.

        Return type:
            Bin
        """
        return self.bins[bin_number]

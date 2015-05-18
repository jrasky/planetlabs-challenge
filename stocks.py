#!/usr/bin/env python
"""find_profit is O(n) over a list, given a window, to find the maximum profit
possible given a single pair of trades taking place in that window"""
import unittest


def find_profit(prices, window):
    """Given a certain window size and a list of prices, find the highest
    profit possible if exactly one share is bought then sold within that
    perid. Returns this profit."""

    # back_prices keeps track of previous prices
    # this is a copy so we don't have to access prices directly
    back_prices = []

    # pivot is the lowest price in the window
    pivot = None

    # next_pivot is the lowest price in the window after pivot
    # this is where pivot is moved if it falls out of the window
    next_pivot = None

    # accumulated maximum profit
    profit = 0

    # this is the only direct access of prices, and only assumes that an
    # __iter__ function is available
    for i, price in enumerate(prices):
        # add the current price to back_prices
        back_prices.append(price)

        # trim the back prices list to only be the window length
        while len(back_prices) > window + 1:
            back_prices.pop(0)

        # test to see if we've found a lower pivot
        if pivot is None or price < back_prices[pivot - i - 1]:
            # set the pivot and the pivot price
            pivot = i
            # bump the next_pivot if we've passed it
            next_pivot = max(next_pivot, pivot + 1)

        # test to see if we've found a lower next_pivot
        if next_pivot is None or (next_pivot <= i and price <
                                  back_prices[next_pivot - i - 1]):
            # set it and the next_price
            next_pivot = i

        # test to see if the pivot has fallen out of the window
        if i - pivot == window:
            # move the pivot to the next position
            pivot = next_pivot
            # set the next_pivot to one after the new pivot
            next_pivot = pivot + 1

        # update the profit accumulator
        profit = max(profit, price - back_prices[pivot - i - 1])

    # return the accumulated profit once done
    return profit

# pylint: disable=R0904
class StockProfitTests(unittest.TestCase):
    """Unit tests for the find_profit function"""

    def test_increase(self):
        """Test an increasing window size with a simple list"""

        self.assertEqual(find_profit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 2), 1.0)

        self.assertEqual(find_profit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 3), 2.0)

        self.assertEqual(find_profit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 4), 3.0)

    def test_window_sizes(self):
        """Test various difficult lists with window sizes larger than the best
        size possible"""

        self.assertEqual(find_profit([1.0, 2.0, 3.0, 1.0, 3.0, 4.0], 5), 3.0)

        self.assertEqual(find_profit([7.0, 5.0, 6.0, 4.0, 5.0, 3.0,
                                      4.0, 2.0, 3.0, 1.0], 5), 1.0)

        self.assertEqual(find_profit([4.0, 3.0, 2.0, 4.0, 3.0, 1.0,
                                      1.1, 1.2, 1.3, 1.4], 5), 2.0)

    def test_shifting(self):
        """Test a growing window, where each increase makes for a different
        profit"""

        self.assertEqual(find_profit([2.0, 3.0, 1.0, 2.0, 4.0, 5.0, 7.0,
                                      8.0], 2), 2.0)

        self.assertEqual(find_profit([2.0, 3.0, 1.0, 2.0, 4.0, 5.0, 7.0,
                                      8.0], 3), 3.0)

        self.assertEqual(find_profit([2.0, 3.0, 1.0, 2.0, 4.0, 5.0, 7.0,
                                      8.0], 4), 5.0)

        self.assertEqual(find_profit([2.0, 3.0, 1.0, 2.0, 4.0, 5.0, 7.0,
                                      8.0], 5), 6.0)

        self.assertEqual(find_profit([2.0, 3.0, 1.0, 2.0, 4.0, 5.0, 7.0,
                                      8.0], 6), 7.0)


if __name__ == "__main__":
    unittest.main()

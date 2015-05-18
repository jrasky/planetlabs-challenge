#!/usr/bin/env python
import unittest


def find_profit(prices, window):
    """Given a certain window size and a list of prices, find the highest
    profit possible if exactly one share is bought then sold within that
    perid. Returns this profit."""

    # pivot is the lowest price in the window
    pivot = None
    # this is the price, so we don't have to index the price list
    pivot_price = None

    # next_pivot is the lowest price in the window after pivot
    # this is where pivot is moved if it falls out of the window
    next_pivot = None
    # this is the price for it, so we don't have to index like above
    next_price = None

    # accumulated maximum profit
    profit = 0

    # this is the only direct access of prices, and only assumes that an
    # __iter__ function is available
    for i, price in enumerate(prices):
        # test to see if we've found a lower pivot
        if pivot is None or price < pivot_price:
            # set the pivot and the pivot price
            pivot = i
            pivot_price = price
            # bump the next_pivot if we've passed it
            if pivot + 1 > next_pivot:
                next_pivot = pivot + 1
                next_price = None

        # set the next_price if we're at that index
        if i == next_pivot:
            next_price = price

        # test to see if we've found a lower next_pivot
        if next_pivot is None or price < next_price:
            # set it and the next_price
            next_pivot = i
            next_price = price

        # test to see if the pivot has fallen out of the window
        if i - pivot == window:
            # move the pivot to the next position
            pivot = next_pivot
            pivot_price = next_price
            # set the next_pivot to one after the new pivot
            next_pivot = pivot + 1
            next_price = None

        # update the profit accumulator
        profit = max(profit, price - pivot_price)

    # return the accumulated profit once done
    return profit


class StockProfitTests(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(find_profit([1.0, 2.0, 3.0, 1.0, 3.0, 4.0], 5), 3.0)

        self.assertEqual(find_profit([7.0, 5.0, 6.0, 4.0, 5.0, 3.0,
                                      4.0, 2.0, 3.0, 1.0], 5), 1.0)

        self.assertEqual(find_profit([4.0, 3.0, 2.0, 4.0, 3.0, 1.0,
                                      1.1, 1.2, 1.3, 1.4], 5), 2.0)


if __name__ == "__main__":
    unittest.main()

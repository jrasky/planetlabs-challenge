#!/usr/bin/env python
import unittest


def find_profit(prices, window):
    pivot = None
    pivot_price = None
    next_pivot = None
    next_price = None
    profit = 0

    for i, price in enumerate(prices):
        if pivot is None or price < pivot_price:
            pivot = i
            pivot_price = price
            if pivot + 1 > next_pivot:
                next_pivot = pivot + 1
                next_price = None

        if i == next_pivot:
            next_price = price

        if next_pivot is None or price < next_price:
            next_pivot = i
            next_price = price

        if i - pivot == window:
            pivot = next_pivot
            pivot_price = next_price
            next_pivot = pivot + 1
            next_price = None

        profit = max(profit, price - pivot_price)

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

#!/usr/bin/env python


def find_points(prices, window):
    pivot = None
    next_pivot = None
    profit = 0

    for i, price in enumerate(prices):
        if pivot is None or price < prices[pivot]:
            pivot = i
            next_pivot = max(next_pivot, pivot + 1)

        if pivot != i and (next_pivot is None or price < prices[next_pivot]):
            next_pivot = i

        if i - pivot == window:
            pivot = next_pivot
            next_pivot = pivot + 1

        profit = max(profit, price - prices[pivot])

    return profit


def main():
    print find_points([1.0, 2.0, 3.0, 1.0, 3.0, 4.0], 5)

    print find_points([7.0, 5.0, 6.0, 4.0, 5.0, 3.0, 4.0, 2.0, 3.0, 1.0], 5)

    print find_points([4.0, 3.0, 2.0, 4.0, 3.0, 1.0, 1.1, 1.2, 1.3, 3.4], 5)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
prices = [4.0, 3.0, 2.0, 4.0, 3.0, 1.0, 1.1, 1.2, 1.3, 1.4]


class ParserState:
    def __init__(self, window):
        self.best_window = []
        self.current_window = []
        self.skipped = []
        self.window = window

    def clear(self):
        self.best_window = []
        self.current_window = []
        self.skipped = []

    def increase(self, price):
        if not self.current_window:
            return True
        elif len(self.current_window) == self.window:
            print "Full window"
            print "Skipped:", self.skipped
            return self.current_window[-1] - self.current_window[0] < \
                price - self.current_window[len(self.skipped) + 1]
        else:
            return self.current_window[-1] < price

    def sift(self):
        if not self.best_window or self.best_window[-1] - self.best_window[0] \
           < self.current_window[-1] - self.current_window[0]:
            self.best_window = self.current_window
        self.current_window = []

    def skip(self, price):
        if len(self.skipped) + 1 == self.window:
            # we've moved forward an entire window
            self.sift()
            self.skipped = []
        elif not self.current_window:
            # nothing to do in this case
            return
        else:
            self.skipped.append(price)

    def unskip(self):
        self.current_window.extend(self.skipped)

    def trim(self):
        while len(self.current_window) > self.window:
            self.current_window.pop(0)

    def insert(self, price):
        if self.increase(price):
            print "Price increase:", price
            self.unskip()
            self.current_window.append(price)
            self.trim()
        else:
            self.skip(price)

    def process(self, prices):
        self.clear()

        for i, price in enumerate(prices):
            if prices[max(0, i - 1)] < price or price \
               < prices[min(i + 1, len(prices) - 1)]:
                print "Inserting:", price
                self.insert(price)
            else:
                print "Skipping:", price
                self.skip(price)

        self.sift()
        return self.best_window


def main():
    parser = ParserState(3)

    best_window = parser.process(prices)

    print best_window

if __name__ == "__main__":
    main()

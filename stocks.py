#!/usr/bin/env python
prices = [1.0, 2.0, 3.0, 5.1, 5.5, 8.5]


def find_points(prices, window):
    best_window = []
    current_window = []
    skipped = []
    offset = 1

    # ideas to make this better:
    # start our windows on increases only
    # consider stopping them on decreases
    # this would allow for subsets smaller than the window to be considered

    for price in prices:
        print "price:", price
        print "best", best_window
        print "current", current_window
        print "skipped", skipped
        print "offset", offset
        print
        if len(current_window) < window:
            current_window.append(price)
        else:
            if current_window[-1] - current_window[0] < \
               price - current_window[offset]:
                for i in xrange(offset):
                    current_window.pop(0)
                current_window.extend(skipped)
                current_window.append(price)
                skipped = []
                offset = 1
            else:
                if offset == window:
                    # we've moved forward an entire window
                    if not best_window or best_window[-1] - best_window[0] < \
                       current_window[-1] - current_window[0]:
                        best_window = current_window
                    current_window = skipped
                    current_window.append(price)
                    skipped = []
                    offset = 1
                else:
                    offset += 1
                    skipped.append(price)

    print "best", best_window
    print "current", current_window
    print "skipped", skipped
    print "offset", offset
    print

    if not best_window or (current_window and best_window[-1] -
                           best_window[0] < current_window[-1] -
                           current_window[0]):
        best_window = current_window

    return best_window


def main():
    window = find_points(prices, 3)

    print window

if __name__ == "__main__":
    main()

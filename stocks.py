#!/usr/bin/env python
prices = [1.0, 2.0, 3.0, 5.1, 5.5, 1.0]


def find_points(prices, window):
    best_window = []
    current_window = []
    offset = 1

    for price in prices:
        print "best", best_window
        print "current", current_window
        print
        if len(current_window) < window:
            current_window.append(price)
        else:
            # there are some issues with the code below
            # updon finding a better window, it needs to pop up to
            # offset and then append the rest of the prices
            # this does not happen as of yet
            if current_window[-1] - current_window[0] < \
               price - current_window[offset]:
                current_window.pop(offset - 1)
                current_window.append(price)
            else:
                offset += 1
                if offset == window:
                    # we've moved forward an entire window
                    if not best_window or best_window[-1] - best_window[0] < \
                       current_window[-1] - current_window[0]:
                        best_window = current_window
                    current_window = [price]
                    offset = 1

    print "best", best_window
    print "current", current_window

    if not best_window or (current_window and best_window[-1] -
                           best_window[0] < current_window[-1] -
                           current_window[0]):
        best_window = current_window

    return best_window


def main():
    window = find_points(prices, 2)

    print window

if __name__ == "__main__":
    main()

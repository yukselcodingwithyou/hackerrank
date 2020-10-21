#!/bin/python3


def simple_array_sum(ar):
    return sum(ar)


if __name__ == '__main__':
    # sum of power of 2 of numbers in range 1, 100 as example
    simple_array_sum([a ** 2 for a in range(100)])

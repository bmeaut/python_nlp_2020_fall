#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Judit Acs <judit@sch.bme.hu>
#
# Distributed under terms of the MIT license.

import sys


def is_prime(N):
    for div in range(2, int(N ** 0.5) + 1):
        if N % div == 0:
            return False
    return True


def get_n_primes(N):
    if N < 0:
        raise ValueError("N must be non-negative.")
    primes = []
    number = 2
    while len(primes) < N:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes


def main():
    assert(get_n_primes(3) == [2, 3, 5])
    print("Tests passed.")
    print("Trying for user input.")
    N = int(input("N = "))
    print(get_n_primes(N))


if __name__ == '__main__':
    main()

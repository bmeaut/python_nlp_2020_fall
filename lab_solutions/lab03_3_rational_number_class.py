#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def gcd(x, y):
    while x % y != 0:
        prev_x = x
        prev_y = y
        x = prev_y
        y = prev_x % prev_y
    return y


class RationalNumberValueError(ValueError):
    pass


class RationalNumber:
    def __init__(self, p, q=1):
        self.validate_numerator(p)
        self.validate_denominator(q)
        self._p = p
        self._q = q
        self.normalize_fraction()
        if self._q < 0:
            self.switch_signs()

    def normalize_fraction(self):
        greatest_common_div = gcd(self.p, self.q)
        if greatest_common_div != 1:
            self._p = self.p // greatest_common_div
            self._q = self.q // greatest_common_div

    def switch_signs(self):
        self._p *= -1
        self._q *= -1

    def __add__(self, other):
        numerator = self.p * other.q + self.q * other.p
        denominator = self.q * other.q
        return RationalNumber(numerator, denominator)

    def __eq__(self, other):
        return (self.p == other.p) and (self.q == other.q)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
        return RationalNumber(self.p * other.p, self.q * other.q)

    def __imul__(self, other):
        return self * other

    def __iadd__(self, other):
        return self + other

    def __idiv__(self, other):
        return self / other

    def __truediv__(self, other):
        return self * other.inverse()

    def __hash__(self):
        return hash((self.p, self.q))

    def __repr__(self):
        return f'{self._p}/{self._q}'

    def __abs__(self):
        return abs(self.p / self.q)

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self.validate_numerator(value)
        self._p = value
        self.normalize_fraction()

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, value):
        self.validate_denominator(value)
        self._q = value
        if value < 0:
            self.switch_signs()
        self.normalize_fraction()

    @staticmethod
    def validate_numerator(cls, p):
        if not isinstance(p, int):
            raise RationalNumberValueError('Numerator has to be an Integer')

    @staticmethod
    def validate_denominator(cls, q):
        if not isinstance(q, int):
            raise RationalNumberValueError('Denominator has to be an Integer')
        if q == 0:
            raise RationalNumberValueError('Cannot set denominator to 0')

    @classmethod
    def from_str(cls, input_str):
        p, q = input_str.split('/')
        return cls(int(p), int(q))

    def inverse(self):
        return RationalNumber(self.q, self.p)


def main():
    # Test basic operators
    r = RationalNumber(43, 2)
    assert r + r == RationalNumber(43)  # q = 1 in this case
    assert r * 2 == r + r
    r1 = RationalNumber(3, 2)
    r2 = RationalNumber(4, 3)
    assert r1 * r2 == RationalNumber(12, 6)
    assert r1 / r2 == RationalNumber(9, 8)
    assert r1 == RationalNumber(6, 4)
    r4 = RationalNumber(2, 3)
    r4.p = 20 * 55
    r4.q = 55
    assert r4 == RationalNumber(20)

    # Test whether class is usable as dict key
    r1 = RationalNumber(3)
    r2 = RationalNumber(3, 1)
    r3 = RationalNumber(3, 2)

    d = {r1: 1, r2: 2, r3: 12}
    assert (len(d) == 2)

    # Test numerator and denominator validation
    try:
        r1.p = 3.4
    except RationalNumberValueError:
        print("This should happen")
    else:
        print("This shouldn't happen")
    try:
        r1.q = 3.4
    except ValueError:
        print("This should happen")
    else:
        print("This shouldn't happen")

    # Test negative number behaviour
    r = RationalNumber(3, -2)
    assert r.p == -3 and r.q == 2
    assert abs(r) == 1.5

    # Test from_str factory method
    r1 = RationalNumber(-3, 2)
    r2 = RationalNumber(12, 34)
    assert RationalNumber.from_str("-3/2") == r1
    assert RationalNumber.from_str("-6/4") == r1
    assert RationalNumber.from_str("12 / 34") == r2
    assert RationalNumber.from_str("36/    102") == r2

    print("Tests passed.")


if __name__ == '__main__':
    main()

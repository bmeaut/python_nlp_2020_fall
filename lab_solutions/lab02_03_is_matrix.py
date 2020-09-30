#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def is_matrix(M):
    if len(M) == 0:
        return True
    else:
        for i in range(1, len(M)):
            if len(M[i]) != len(M[0]):
                return False

        return True


def main():
    assert is_matrix([]) == True
    assert is_matrix([[], []]) == True
    assert is_matrix([[1, 2], [2, 1]]) == True
    assert is_matrix([[1], [2, 1]]) == False
    assert is_matrix([[1, 2], [2, 1], [3, 4]]) == True
    assert is_matrix([[1, 2], [2, 1], [3, 4, 5]]) == False

    print("Tests passed.")


if __name__ == '__main__':
    main()

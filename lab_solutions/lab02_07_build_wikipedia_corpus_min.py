#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Bence Bial <gbenceg@gmail.com>
#
# Distributed under terms of the MIT license.

import wikipedia


def build_wikipedia_corpus(min_char=10_000):
    corpus = []
    corp_len = 0

    for city in ["Budapest", "Vienna", "Seattle", "Dublin"]:
        page = wikipedia.page(city)
        corpus.append(page.content)
        corp_len += len(page.content)

        if corp_len >= min_char:
            break

    return corpus


def main():
    corpus = build_wikipedia_corpus(1000)

    # check types
    assert isinstance(corpus, list)
    assert isinstance(corpus[0], str)

    # check character count
    sum_length = 0
    for document in corpus:
        sum_length += len(document)
    assert sum_length >= 1000
    # shouldn't be too long
    assert sum_length < 100000

    print("Tests passed.")


if __name__ == '__main__':
    main()

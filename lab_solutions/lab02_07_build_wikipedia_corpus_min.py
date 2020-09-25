#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

import wikipedia


def build_wikipedia_corpus_min(min_char=10000):
    # Maybe I misunderstood this task, but this is almost the same as the previous one, to my understanding.
    wikipedia.set_lang('hu')
    cities_to_search = ['Budapest', 'Debrecen', 'Miskolc', 'Nyíregyháza', 'Pécs', 'Szeged']
    corpus_length = 0
    corpus = []
    for city in cities_to_search:
        city_page = wikipedia.page(city)
        if corpus_length < min_char:
            corpus.append(city_page.content)
            corpus_length += len(city_page.content)
        else:
            return corpus


def main():
    corpus = build_wikipedia_corpus_min(1000)

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

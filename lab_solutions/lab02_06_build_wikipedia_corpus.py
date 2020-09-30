#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

import wikipedia


def build_wikipedia_corpus():
    wikipedia.set_lang('hu')
    cities_to_search = ['Budapest', 'Debrecen', 'Miskolc',
                        'Nyíregyháza', 'Pécs', 'Szeged']
    corpus_length = 0
    corpus = []
    for city in cities_to_search:
        city_page = wikipedia.page(city)
        if corpus_length <= 100000:
            corpus.append(city_page.content)
            corpus_length += len(city_page.content)
        else:
            return corpus

    raise Exception('Could not exceed the desired 100000 corpus length. '
                    'Please provide more pages to search.')


def main():
    corpus = build_wikipedia_corpus()

    # check types
    assert isinstance(corpus, list)
    assert isinstance(corpus[0], str)

    # check character count
    sum_length = 0
    for document in corpus:
        sum_length += len(document)
    assert sum_length >= 100000

    print("Tests passed.")


if __name__ == '__main__':
    main()

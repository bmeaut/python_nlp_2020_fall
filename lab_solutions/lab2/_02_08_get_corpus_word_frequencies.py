#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab2._02_05_word_freq import word_freq
from lab_solutions.lab2._02_06_build_wikipedia_corpus import build_wikipedia_corpus


def get_and_pretty_print_top_k(freq_dict, k=10):
    list_to_print = sorted(list(freq_dict.items()), key=lambda x: x[1], reverse=True)[:k]
    for key, value in list_to_print:
        print(key + '\t' + str(value))

    return list_to_print


def construct_test_case():
    corpus = []
    base_text = 'This lecture is really cool. Please give me extra points. I really need them. :)'
    corpus.append(base_text)
    animals = ['dog', 'cat', 'bird', 'elephant', 'monkey', 'mice', 'donkey', 'lion', 'medusa', 'whale', 'eagle', 'pig', 'chicken']
    for i in range(len(animals)):
        animal_text = ''.join([animals[i] + ' ' for j in range(i+1)])
        text = f'This sentence contains {i+1} of the same words: ' + str(animal_text)
        corpus.append(text)

    return corpus


def get_corpus_word_frequencies(corpus):
    base_dict = {}
    for text in corpus:
        freqs = word_freq(text)
        base_dict = {x: base_dict.get(x, 0) + freqs.get(x, 0) for x in set(base_dict.keys()).union(set(freqs.keys()))}

    top_k = get_and_pretty_print_top_k(base_dict)
    return top_k


def main():
    corpus = build_wikipedia_corpus()
    _ = get_corpus_word_frequencies(corpus)
    print('------------------------')
    test_case = construct_test_case()
    test_case_word_freqs = get_corpus_word_frequencies(test_case)
    expected_result = [('This', 14),
                       ('chicken', 13),
                       ('sentence', 13),
                       ('of', 13),
                       ('contains', 13),
                       ('the', 13),
                       ('words:', 13),
                       ('same', 13),
                       ('pig', 12),
                       ('eagle', 11)]
    # Converting the lists to sets here, so in case two words have equal frequency in the top 10, the ordering won't have an effect on the tests
    assert (set(test_case_word_freqs) == set(expected_result))

    print("Test passed.")


if __name__ == '__main__':
    main()

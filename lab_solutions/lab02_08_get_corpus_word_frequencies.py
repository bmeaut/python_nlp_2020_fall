#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab02_06_build_wikipedia_corpus import build_wikipedia_corpus


def get_top_k(freq_dict, k=10):
    return sorted(list(freq_dict.items()), key=lambda x: x[1], reverse=True)[:k]


def pretty_print_top_k(list_to_print):
    for key, value in list_to_print:
        print(f'{key} \t {str(value)}')


def construct_test_case():
    corpus = []
    base_text = 'This lecture is really cool. Please give me extra points. I really need them. :)'
    corpus.append(base_text)
    animals = ['dog', 'cat', 'bird', 'elephant', 'monkey', 'mice', 'donkey', 'lion', 'medusa', 'whale', 'eagle', 'pig', 'chicken']
    for i in range(len(animals)):
        animal_text = ''.join([animals[i] + ' ' for _ in range(i+1)])
        text = f'This sentence contains {i+1} of the same words: {str(animal_text)[:-1]}'
        corpus.append(text)

    return corpus


def get_corpus_word_frequencies(corpus):
    base_dict = {}
    for text in corpus:
        for word in text.split(" "):
            if word not in base_dict:
                base_dict[word] = 1
            else:
                base_dict[word] += 1
    top_k = get_top_k(base_dict)
    return top_k


def main():
    corpus = build_wikipedia_corpus()
    corpus_freqs = get_corpus_word_frequencies(corpus)
    pretty_print_top_k(corpus_freqs)
    print('------------------------')
    test_case = construct_test_case()
    test_case_word_freqs = get_corpus_word_frequencies(test_case)
    pretty_print_top_k(test_case_word_freqs)
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

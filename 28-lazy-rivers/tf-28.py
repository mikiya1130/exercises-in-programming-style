#!/usr/bin/env python
import operator
import string
import sys


def characters(filename):
    for line in open(filename, encoding="utf-8"):
        for c in line:
            yield c


def all_words(filename):
    start_char = True
    for c in characters(filename):
        if start_char is True:
            word = ""
            if c.isalnum():
                word = c.lower()
                start_char = False
            else:
                pass
        else:
            if c.isalnum():
                word += c.lower()
            else:
                start_char = True
                yield word


def non_stop_words(filename):
    stopwords = set(open("../stop_words.txt").read().split(",") + list(string.ascii_lowercase))
    for w in all_words(filename):
        if w not in stopwords:
            yield w


def count_and_sort(filename):
    freqs, i = {}, 1
    for w in non_stop_words(filename):
        freqs[w] = 1 if w not in freqs else freqs[w] + 1
        if i % 5000 == 0:
            yield sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)
        i = i + 1
    yield sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)


for word_freqs in count_and_sort(sys.argv[1]):
    print("-----------------------------")
    for w, c in word_freqs[0:25]:
        print(w, "-", c)

#!/usr/bin/env python
import collections
import operator
import re
import sys


class WordFrequenciesModel:
    freqs = {}
    stopwords = set(open("../stop_words.txt").read().split(","))

    def __init__(self, path_to_file):
        self.update(path_to_file)

    def update(self, path_to_file):
        try:
            words = re.findall(r"[a-z]{2,}", open(path_to_file, encoding="utf-8").read().lower())
            self.freqs = collections.Counter(w for w in words if w not in self.stopwords)
        except IOError:
            print("File not found")
            self.freqs = {}


class WordFrequenciesView:
    def __init__(self, model):
        self._model = model

    def render(self):
        sorted_freqs = sorted(self._model.freqs.items(), key=operator.itemgetter(1), reverse=True)
        for w, c in sorted_freqs[0:25]:
            print(w, "-", c)


class WordFrequencyController:
    def __init__(self, model, view):
        self._model, self._view = model, view
        view.render()

    def run(self):
        while True:
            print("Next file: ")
            sys.stdout.flush()
            filename = sys.stdin.readline().strip()
            self._model.update(filename)
            self._view.render()


m = WordFrequenciesModel(sys.argv[1])
v = WordFrequenciesView(m)
c = WordFrequencyController(m, v)
c.run()

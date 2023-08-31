#!/usr/bin/env python
import operator
import os
import re
import string
import sys
import threading
from time import sleep

from util import cls, get_input, getch

lock = threading.Lock()


class FreqObserver(threading.Thread):
    def __init__(self, freqs):
        super().__init__()
        self.daemon, self._end = True, False
        self._freqs = freqs
        self._freqs_0 = sorted(self._freqs.items(), key=operator.itemgetter(1), reverse=True)[:25]
        self.start()

    def run(self):
        while not self._end:
            self._update_view()
            sleep(0.1)
        self._update_view()

    def stop(self):
        self._end = True

    def _update_view(self):
        lock.acquire()
        freqs_1 = sorted(self._freqs.items(), key=operator.itemgetter(1), reverse=True)[:25]
        lock.release()
        if freqs_1 != self._freqs_0:
            self._update_display(freqs_1)
            self._freqs_0 = freqs_1

    def _update_display(self, tuples):
        def refresh_screen(data):
            cls()
            print(data)
            sys.stdout.flush()

        data_str = ""
        for w, c in tuples:
            data_str += str(w) + " - " + str(c) + "\n"
        refresh_screen(data_str)


class WordsCounter:
    freqs = {}

    def count(self):
        def non_stop_words():
            stopwords = set(
                open("../stop_words.txt").read().split(",") + list(string.ascii_lowercase)
            )
            for line in f:
                yield [w for w in re.findall(r"[a-z]{2,}", line.lower()) if w not in stopwords]

        words = next(non_stop_words())
        lock.acquire()
        for w in words:
            self.freqs[w] = 1 if w not in self.freqs else self.freqs[w] + 1
        lock.release()


print("Press space bar to fetch words from the file one by one")
print("Press ESC to switch to automatic mode")
model = WordsCounter()
view = FreqObserver(model.freqs)
with open(sys.argv[1], encoding="utf-8") as f:
    while get_input():
        try:
            model.count()
        except StopIteration:
            view.stop()
            sleep(1)
            break

#!/usr/bin/env python
import collections
import re
import sys

stops = open("../stop_words.txt").read().split(",")
words = re.findall(r"[a-z]{2,}", open(sys.argv[1], encoding="utf-8").read().lower())
counts = collections.Counter(w for w in words if w not in stops)
for w, c in counts.most_common(25):
    print(w, "-", c)

import re
import string
import sys


def extract_words(path_to_file):
    words = re.findall("[a-z]{2,}", open(path_to_file, encoding="utf-8").read().lower())
    stopwords = set(open("../stop_words.txt").read().split(","))
    return [w for w in words if w not in stopwords]

import re
import string
import sys


def extract_words(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        str_data = f.read()
    pattern = re.compile(r"[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()

    with open("../stop_words.txt") as f:
        stop_words = f.read().split(",")
    stop_words.extend(list(string.ascii_lowercase))

    return [w for w in word_list if w not in stop_words]

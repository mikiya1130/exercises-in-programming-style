from functools import reduce

print(
    reduce(
        lambda string, tup: string + tup[0] + " - " + str(tup[1]) + "\n",
        sorted(
            filter(
                lambda tup: tup[0]
                not in open(
                    __import__("os").path.join(
                        __import__("os").path.dirname(__file__), "..", "stop_words.txt"
                    )
                )
                .read()
                .lower()
                .split(","),
                reduce(
                    lambda word_dict, word: word_dict
                    if (word_dict.__setitem__(word, word_dict.get(word, 0) + 1) if True else None)
                    else word_dict,
                    filter(
                        lambda word: len(word) > 1,
                        (
                            "".join(
                                map(
                                    lambda letter: " "
                                    if ord(letter) not in set(range(ord("a"), ord("z") + 1))
                                    else letter,
                                    open(__import__("sys").argv[1]).read().lower(),
                                )
                            )
                        ).split(),
                    ),
                    {},
                ).items(),
            ),
            key=lambda tup: tup[1],
            reverse=True,
        )[0:25],
        "",
    )
)  # hole in one?

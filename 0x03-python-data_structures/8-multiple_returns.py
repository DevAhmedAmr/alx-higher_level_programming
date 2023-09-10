#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence is not None:
        str_len = len(sentence)

    if sentence is None or str_len == 0:
        return (0, None)

    first_char = sentence[0]

    return (str_len, first_char)

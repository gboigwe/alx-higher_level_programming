#!/usr/bin/python3
"""
Defines text_indentation
Checking certain characters before printing.
"""


def text_indentation(text):
    """Display these text with two newlines
    after these characters {'.', '?', ':'}.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delims in ":.?":
        text = (delims + "\n\n").join(
            [i.strip(" ") for i in text.split(delims)])
    print("{}".format(text), end="")

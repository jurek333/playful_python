#!/usr/bin/env python3
"""Password maker"""

import argparse
import os
import sys
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='*',
                        help='Input file(s)',
                        default=[open('/usr/share/dict/words')])

    parser.add_argument('-n',
                        '--num',
                        metavar='INT',
                        type=int,
                        default=3,
                        help='Number of passwords to generate')

    parser.add_argument('-w',
                        '--num_words',
                        metavar='INT',
                        type=int,
                        default=4,
                        help='Number of words to use for password')

    parser.add_argument('-m',
                        '--min_word_len',
                        metavar='INT',
                        type=int,
                        default=3,
                        help='Minimum word length')

    parser.add_argument('-s',
                        '--seed',
                        metavar='INT',
                        type=int,
                        help='Random seed')

    parser.add_argument('-l',
                        '--l33t',
                        action='store_true',
                        help='Obsfuscate letters')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    clean = lambda word: re.sub('[^a-zA-Z]', '', word)
    for fh in args.file:
        for word in filter(lambda w: len(w) > args.min_word_len,
                           map(clean,
                               fh.read().lower().split())):
            words.add(word.title())

    words = sorted(list(words))

    for _ in range(args.num):
        password = ''.join(random.sample(words, args.num_words))
        print(l33t(password) if args.l33t else password)


# --------------------------------------------------
def l33t(text):
    """l33t"""

    text = ransom(text)
    xform = {
        'a': '@',
        'A': '4',
        'o': '0',
        'O': '0',
        't': '+',
        'e': '3',
        'E': '3',
        'I': '1',
        'S': '5'
    }
    for x, y in xform.items():
        text = text.replace(x, y)

    return text


# --------------------------------------------------
def ransom(text):
    """Randomly choose an upper or lowercase letter to return"""

    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


# --------------------------------------------------
if __name__ == '__main__':
    main()

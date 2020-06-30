#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    actions = ['rock', 'paper', 'scissors']
    res = [[[]], [['rock'], ['paper'], ['scissors']]]
    for i in range(2, n+1):
        cur = []
        for match in res[i-1]:
            for action in actions:
                tmp = match.copy()
                tmp.append(action)
                cur.append(tmp)
        res.append(cur)
    return res[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

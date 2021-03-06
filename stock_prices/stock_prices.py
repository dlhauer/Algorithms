#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = 0
    min_price = 10 ** 64
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    if max_profit == 0:
        min_loss = -10 ** 64
        for i in range(len(prices)-1):
            min_loss = max(min_loss, prices[i + 1] - prices[i])
        return min_loss
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

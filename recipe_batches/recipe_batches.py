#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    cur_max = 10 ** 100
    for key, value in recipe.items():
        if key not in ingredients or cur_max == 0:
            return 0
        cur_max = min(cur_max, ingredients[key] // value)
    return cur_max

# The above implementation isn't *guaranteed* to work. It will fail
# if the maximum batches possible exceeds 10 ** 100. The implementation
# below is guaranteed to work, but it allocates an additional list
# in memory. Trade-offs, ya know?


def recipe_batches_two(recipe, ingredients):
    maxes = []
    batches = 1
    for key, value in recipe.items():
        if batches == 0 or key not in ingredients:
            return 0
        batches = ingredients[key] // value
        maxes.append(batches)
    return min(maxes)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 99, 'butter': 200, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches_two(recipe, ingredients), ingredients=ingredients))

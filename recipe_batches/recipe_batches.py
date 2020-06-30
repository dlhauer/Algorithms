#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
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
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

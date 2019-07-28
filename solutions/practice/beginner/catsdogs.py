#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem

    Chef is a farmer and a pet lover. He has a lot of his favorite pets cats
    and dogs in the barn. He knows that there are 'C' cats and 'D' dogs in the
    barn. Also, one day went to field and found that there were 'L' legs of the
    animals touching the ground. Chef knows that cats love to ride on the dogs.
    So, they might ride on the dogs, and their legs won't touch the ground and
    Chef would miss counting their legs. Chef's dogs are strong enough to ride
    at max two cats on their back.

    It was cold foggy morning, when Chef did this counting. So he is now
    wondering whether he counted the legs properly or not. Specifically, he is
    wondering is there a some possibility of his counting being correct. Please
    help Chef in finding it.

Input

    First line of the input contains an integer 'T' denoting number of test
    cases. 'T' test cases follow.

    The only line of each test case contains three space separated integers C,
    D, L denoting number of the cats, number of the dogs and number of legs of
    animals counted by Chef, respectively.

Output

    For each test case, output a single line containing a string 'yes', 'no'
    (both without quotes) according to the situation.

Constraints

    * 1 <= T <= 10^5
    * 0 <= C, D, L <= 10^9

Subtasks

    Subtask # 1

        * 1 <= T <= 10^4
        * 0 <= C, D <= 10^2

    Subtask # 2

        * 1 <= T <= 10^5
        * 0 <= C, D <= 10^3

    Subtask # 3

        * Original constraints

Example

    Inputs

        3
        1 1 8
        1 1 4
        1 1 2

    Output

        yes
        yes
        no

Explanation

    Example 1

        There is one cat and one dog. The number of legs of these animals on
        the ground are 8, it can be possible when both cat and dog are standing
        on the ground.

    Example 2

        There is one cat and dog. The number of legs of these animals on the
        ground are 4, it can be possible if the cat will ride on the dog, so
        its legs won't be counted by Chef, only the dog's legs will be counted.

    Example 3

        There is one cat and one dog. The number of legs of these animals are
        2, it can not be true at all, Chef might have made some mistake. Hence
        answer is "no".
"""


def _is_negative(number):
    return (number < 0)


def verify(
    number_of_cats: int, number_of_dogs: int, counted_legs: int
) -> bool:
    """Verify counted legs

    This method verifies that counted legs are correct or not based on given
    number of cats and number of dogs. Each cat and dog will have a four legs.

    According to the problem statement, maximum two cats can climb on a dog.
    Which opens three state for each dog

        1. No cat is climbing on a dog.
        2. One cat is climbing on a dog. Here, leg of one cat will be less from
           counted legs.
        3. Two cats are climbing on a dog. Here, leg of two cats will be less
           form counted legs.
    """
    if _is_negative(number_of_cats) or _is_negative(number_of_dogs):
        return False
    total_legs = (number_of_cats + number_of_dogs) * 4
    if total_legs == counted_legs:
        return True
    if total_legs >= counted_legs:
        if verify(number_of_cats - 1, number_of_dogs, counted_legs):
            return True
        elif verify(number_of_cats - 2, number_of_dogs, counted_legs):
            return True
    return False

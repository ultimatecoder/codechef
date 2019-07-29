#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..catsdogs import verify


def test_verify():
    sample_combinations_and_expected_answers = (
        (0, 0, 10, False),
        (1, 1, 8, True),
        (1, 1, 4, True),
        (1, 1, 2, False),
        (0, 1, 4, True),
        (1, 0, 4, True),
        (2, 1, 4, True),
        (0, 2, 4, False),
        (10, 8, 33, False),
        (10, 8, 36, True),
        (25, 1, 4, False),
    )
    for number_of_cats, number_of_dogs, counted_legs, expected_result in (
        sample_combinations_and_expected_answers
    ):
        assert verify(
            number_of_cats,
            number_of_dogs,
            counted_legs
        ) == expected_result

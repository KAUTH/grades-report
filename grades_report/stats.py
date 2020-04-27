#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

from statistics import mean


def mean_grade(parsed_list, passing_grade, overall_mean=True):
    """
    This function calculates the arithmetic mean of the given grades.

    :param parsed_list: the parsed list of the grades
    :param passing_grade: the grade passing threshold
    :param overall_mean: True, when calculating the mean of all the grades,
    False, when calculating the mean of the passing grades
    :return: the arithmetic mean of the given as input parsed list
    """
    if overall_mean is False:
        passing_grades_list = (
            [item for item in parsed_list if item >= passing_grade]
        )
        mean_value = mean(passing_grades_list)

    else:
        mean_value = mean(parsed_list)

    return mean_value

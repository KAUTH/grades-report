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


def total_graded(parsed_list):
    """
    This function finds the total number of individuals that were graded.

    :param parsed_list: the parsed list of the grades
    :return: the total number of people graded
    """
    number_graded = len(parsed_list)

    return number_graded


def total_passed(parsed_list, passing_grade):
    """
    This function finds the total number of individuals that scored over or
    equal to the passing grade.

    :param parsed_list: the parsed list of the grades
    :return: the total number of people graded
    """
    passing_grades_list = (
        [item for item in parsed_list if item >= passing_grade]
    )
    number_passed = len(passing_grades_list)

    return number_passed


def relative_grade_percentage(
    parsed_list, passing_grade, personal_grade, overall_percentage=True
):
    """
    This function calculates the percentage of people that the user's grade
    is above. If overall_percentage is True, then it calculates the above
    taking into account all the grades, otherwise it only considers the passing
    grades.

    :param parsed_list: the parsed list of the grades
    :param passing_grade: the grade passing threshold
    :param overall_percentage: True, when taking into account all the grades,
    False, when considering only the passing grades
    :return: the percentage of grades that you scored above of
    """

    if overall_percentage is False:
        passing_grades_list = (
            [item for item in parsed_list if item >= passing_grade]
        )
        total_grades = len(passing_grades_list)

        lower_grades = (
            [item for item in passing_grades_list if personal_grade > item]
        )

    else:
        total_grades = len(parsed_list)

        lower_grades = (
            [item for item in parsed_list if personal_grade > item]
        )

    total_lower_grades = len(lower_grades)
    relative_grade_percentage = (total_lower_grades / total_grades) * 100

    return relative_grade_percentage

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

from statistics import mean, stdev


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

        if len(passing_grades_list) > 0:
            mean_value = mean(passing_grades_list)

        else:
            mean_value = 0.0

    else:
        mean_value = mean(parsed_list)

    return mean_value


def stdev_grade(parsed_list, passing_grade, overall_stdev=True):
    """
    This function calculates the standard deviation of the given grades.

    :param parsed_list: the parsed list of the grades
    :param passing_grade: the grade passing threshold
    :param overall_stdev: True, when calculating the standard deviation of all
    the grades, False, when calculating the standard deviation of the passing
    grades
    :return: the standard deviation of the given as input parsed list
    """
    if overall_stdev is False:
        passing_grades_list = (
            [item for item in parsed_list if item >= passing_grade]
        )

        if len(passing_grades_list) > 1:
            stdev_value = stdev(passing_grades_list)

        else:
            stdev_value = "- (requires at least two data points)"

    else:
        stdev_value = stdev(parsed_list)

    return stdev_value


def maximum_grade(parsed_list, passing_grade, overall_max=True):
    """
    This function calculates the maximum grade from the given grades.

    :param parsed_list: the parsed list of the grades
    :param passing_grade: the grade passing threshold
    :param overall_max: True, when calculating the maximum of all the grades,
    False, when calculating the maximum of the passing grades
    :return: the maximum element of the given as input parsed list
    """
    if overall_max is False:
        passing_grades_list = (
            [item for item in parsed_list if item >= passing_grade]
        )

        if len(passing_grades_list) > 0:
            max_value = max(passing_grades_list)

        else:
            max_value = "-"

    else:
        max_value = max(parsed_list)

    return max_value


def minimum_grade(parsed_list, passing_grade, overall_min=True):
    """
    This function calculates the minimum grade from the given grades.

    :param parsed_list: the parsed list of the grades
    :param passing_grade: the grade passing threshold
    :param overall_min: True, when calculating the minimum of all the grades,
    False, when calculating the minimum of the passing grades
    :return: the minimum element of the given as input parsed list
    """
    if overall_min is False:
        passing_grades_list = (
            [item for item in parsed_list if item >= passing_grade]
        )

        if len(passing_grades_list) > 0:
            min_value = min(passing_grades_list)

        else:
            min_value = "-"

    else:
        min_value = min(parsed_list)

    return min_value


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

    if (total_grades > 0):
        relative_grade_percentage = (total_lower_grades / total_grades) * 100

    else:
        relative_grade_percentage = 0.0

    return relative_grade_percentage


def grade_distribution(parsed_list, max_grade, bin_number=10):
    """
    This funtion calculates the distribution of the given grades by splitting
    them into 'n' equal bins (intervals) and finding the number of grades
    corresponding to each bin. The bins are left-closed, right-open:
    [a, b) = x | a <= x < b, except from the last one that is closed:
    [c, d] = x | c <= x <= d.

    :param parsed_list: the parsed list of the grades
    :param max_grade: the maximum grade that you can score
    :param bin_number: the number of bins that is calculated in the
    distribution, default is 10
    :return: a list of the number of grades in each bin
    """
    bin_length = max_grade / bin_number
    grade_distribution_list = [0] * bin_number

    for item in parsed_list:
        index = int(item / bin_length)

        if index == bin_number:
            grade_distribution_list[index-1] = (
                grade_distribution_list[index-1] + 1
            )

        else:
            grade_distribution_list[index] = grade_distribution_list[index] + 1

    return grade_distribution_list

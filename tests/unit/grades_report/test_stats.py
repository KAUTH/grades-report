#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

from grades_report.stats import (
    grade_distribution,
    maximum_grade,
    mean_grade,
    minimum_grade,
    relative_grade_percentage,
    stdev_grade,
    total_graded,
    total_passed
)


def test_mean_grade():
    parsed_list = [2, 4, 6, 8]
    passing_grade = 5

    expected = 5
    result = mean_grade(parsed_list, passing_grade, True)

    assert result == expected

    expected = 7
    result = mean_grade(parsed_list, passing_grade, False)

    assert result == expected


def test_stdev_grade():
    parsed_list = [2, 4, 6, 8]
    passing_grade = 5

    expected = 2.581988897471611
    result = stdev_grade(parsed_list, passing_grade, True)

    assert result == expected

    expected = 1.4142135623730951
    result = stdev_grade(parsed_list, passing_grade, False)

    assert result == expected


def test_max_grade():
    parsed_list = [2, 4, 6, 8]
    passing_grade = 5

    expected = 8
    result = maximum_grade(parsed_list, passing_grade, True)

    assert result == expected

    expected = 8
    result = maximum_grade(parsed_list, passing_grade, False)

    assert result == expected


def test_min_grade():
    parsed_list = [2, 4, 6, 8]
    passing_grade = 5

    expected = 2
    result = minimum_grade(parsed_list, passing_grade, True)

    assert result == expected

    expected = 6
    result = minimum_grade(parsed_list, passing_grade, False)

    assert result == expected


def test_total_graded():
    parsed_list = [2, 4, 6, 8]

    expected = 4
    result = total_graded(parsed_list)

    assert result == expected


def test_total_passed():
    parsed_list = [2, 4, 5, 8]
    passing_grade = 5

    expected = 2
    result = total_passed(parsed_list, passing_grade)

    assert result == expected


def test_relative_grade_percentage():
    parsed_list = [2, 4, 5, 6, 7]
    passing_grade = 5
    personal_grade = 6

    overall_percentage = True

    expected = 60
    result = relative_grade_percentage(
        parsed_list, passing_grade, personal_grade, overall_percentage
    )

    assert result == expected

    overall_percentage = False

    expected = (1 / 3) * 100
    result = relative_grade_percentage(
        parsed_list, passing_grade, personal_grade, overall_percentage
    )

    assert result == expected


def test_grade_distribution():
    parsed_list = [0, 2, 4, 5, 5.2, 6, 7, 7.8, 10]
    max_grade = 10

    expected = [1, 0, 1, 0, 1, 2, 1, 2, 0, 1]
    result = grade_distribution(parsed_list, max_grade)

    assert result == expected

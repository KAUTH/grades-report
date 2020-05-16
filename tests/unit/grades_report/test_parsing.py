#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

from unittest import mock
import os

from grades_report.parsing import (
    check_grade_attributes,
    check_grades_list,
    check_personal_grade,
    parse_file,
    parse_user_input
)


def test_check_grade_attributes():
    max_grade_str = "10"
    passing_grade_str = "5"
    grade_attributes = {"max_grade": 10, "passing_grade": 5}

    assert check_grade_attributes(max_grade_str, passing_grade_str) == (
        grade_attributes
    )
    assert check_grade_attributes() == grade_attributes

    not_a_number = "@"
    error = "\nError: @ is not a number!"

    assert check_grade_attributes(not_a_number, passing_grade_str) == error
    assert check_grade_attributes(max_grade_str, not_a_number) == error

    max_grade_str = "10"
    passing_grade_str = "11"
    error = "\nError: Passing grade cannot be greater than the maximum grade!"

    assert check_grade_attributes(max_grade_str, passing_grade_str) == error

    negative_number = "-5"
    error = (
        "\nError: Maximum and passing grade cannot be smaller or equal to " +
        "zero!"
    )

    assert check_grade_attributes(negative_number, passing_grade_str) == error
    assert check_grade_attributes(max_grade_str, negative_number) == error

    max_grade_str = "20"
    grade_attributes = {"max_grade": 20, "passing_grade": 10}

    assert check_grade_attributes(max_grade_str) == grade_attributes

    passing_grade_str = "10"

    assert check_grade_attributes(None, passing_grade_str) == (
        grade_attributes
    )

    grade_attributes = {"max_grade": 10, "passing_grade": 5}

    assert check_grade_attributes() == grade_attributes


def test_check_grades_list():
    list_with_letters = "[1, a, 2]"
    list_with_negatives = [1, -3, 5]
    list_with_max_error = [1, 2, 12]
    correct_list = [1, 2, 3]

    max_grade = 10

    assert check_grades_list(list_with_letters, max_grade) == (
        "\nError:  a is not a number!"
    )

    assert check_grades_list(list_with_negatives, max_grade) == (
        "\nError: -3.0 is not a positive number!"
    )

    assert check_grades_list(list_with_max_error, max_grade) == (
        "\nError: 12.0 is a number greater than the max grade!"
    )

    assert check_grades_list(correct_list, max_grade) == correct_list


def test_check_personal_grade():
    personal_grade_str = 5

    expected = 5
    result = check_personal_grade(personal_grade_str)

    assert result == expected

    personal_grade_str = "a"

    expected = "\nError: a is not a number!"
    result = check_personal_grade(personal_grade_str)

    assert result == expected


def test_parse_file():
    file_path = os.path.join(
        os.getcwd(), "tests/unit/grades_report/grades.csv"
    )
    delimiter = ","

    expected = ["4", "4.6", "5", "8", "10"]
    result = parse_file(file_path, delimiter)

    assert result == expected


@mock.patch("grades_report.parsing.check_grade_attributes")
@mock.patch("grades_report.parsing.check_grades_list")
def test_parse_user_input(
    mock_check_grades_list, mock_check_grades_attributes
):
    file_grades = ("False", ",")
    grades_list = "[1, 2, 3]"
    max_grade_str = "10"
    passing_grade_str = "5"
    personal_grade_input = 0

    max_grade = float(max_grade_str)
    passing_grade = float(passing_grade_str)
    personal_grade = None
    checked_list = [1, 2, 3]

    expected = {
        "checked_list": checked_list,
        "max_grade": max_grade,
        "passing_grade": passing_grade,
        "personal_grade": personal_grade
    }

    mock_check_grades_attributes.return_value = {
        "max_grade": max_grade, "passing_grade": passing_grade
    }

    mock_check_grades_list.return_value = checked_list

    result = parse_user_input(
        file_grades,
        grades_list,
        max_grade_str,
        passing_grade_str,
        personal_grade_input
    )

    assert result == expected

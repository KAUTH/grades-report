#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

import click

from grades_report.parsing import parse_user_input
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

# TO-DO: Add tests for the CLI


def cli_output(user_input):
    """
    This function is responsible for the content that appears printed in the
    CLI of the user.

    :param user_input: a dictionary with the values of the user's input after
    the appropriate validation
    """
    checked_list = user_input["checked_list"]
    max_grade = user_input["max_grade"]
    passing_grade = user_input["passing_grade"]
    personal_grade = user_input["personal_grade"]

    if checked_list is None or max_grade is None or passing_grade is None:
        error = "\nTry \"grades-report --help\"."
        print(error)

        return error

    number_graded = total_graded(checked_list)
    number_passed = total_passed(checked_list, passing_grade)
    number_failed = number_graded - number_passed

    mean_passing_grades = mean_grade(checked_list, passing_grade, False)
    mean_total_grades = mean_grade(checked_list, passing_grade, True)

    stdev_passing_grades = stdev_grade(checked_list, passing_grade, False)
    stdev_total_grades = stdev_grade(checked_list, passing_grade, True)

    # max_passing_grade = maximum_grade(checked_list, passing_grade, False)
    max_total_grade = maximum_grade(checked_list, passing_grade, True)

    min_passing_grade = minimum_grade(checked_list, passing_grade, False)
    min_total_grade = minimum_grade(checked_list, passing_grade, True)

    print(f"\n# Graded: {number_graded}")
    print(f"# Passed: {number_passed}")
    print(f"# Failed: {number_failed}\n")

    print("----------------------------------------------------- \n")

    print(f"Arithmetic Mean of PASSING GRADES: {mean_passing_grades}")
    print(f"Arithmetic Mean of TOTAL GRADES: {mean_total_grades}\n")

    print(f"Standard Deviation of PASSING GRADES: {stdev_passing_grades}")
    print(f"Standard Deviation of TOTAL GRADES: {stdev_total_grades}\n")

    print(f"Max TOTAL GRADE: {max_total_grade}")
    print(
        f"Min PASSING GRADE: {min_passing_grade} & Min TOTAL GRADE: " +
        f"{min_total_grade}"
    )

    if personal_grade is not None:
        overall_relative_grade_percentage = relative_grade_percentage(
            checked_list, passing_grade, personal_grade, True
        )
        passing_relative_grade_percentage = relative_grade_percentage(
            checked_list, passing_grade, personal_grade, False
        )

        print("\n-----------------------------------------------------")
        print(f"\nYour grade: {personal_grade}")
        print(
            f"You scored above {overall_relative_grade_percentage}% of all " +
            "the grades."
        )
        print(
            f"You scored above {passing_relative_grade_percentage}% of the " +
            "passing grades."
        )

    bin_number = 10
    bin_length = max_grade / bin_number
    grade_distribution_list = grade_distribution(
        checked_list, max_grade, bin_number
    )

    print("\n-----------------------------------------------------")
    print("\nGRADE       TOTAL")

    for bin in range(0, bin_number - 1):
        print(
            f"[{bin * bin_length}-{bin * bin_length + bin_length})" +
            f"      {grade_distribution_list[bin]}"
        )

    print(
        f"[{(bin_number - 1) * bin_length}-{bin_number * bin_length}]" +
        f"     {grade_distribution_list[bin_number - 1]}"
    )


@click.command()
@click.option(
    '--file-grades',
    "-f",
    default=("False", ","),
    type=(str, str),
    help=(
        "The path of the file that the grades are to be inserted from, " +
        "followed by a space and the delimiter for the file. For the path " +
        "in Windows make sure to use double backslashes, \\\\, or a single " +
        "forward slash, /."
        )
    )
@click.option(
    "--grades-list",
    "-l",
    default="False",
    help=(
        "A list of the grades. Provide it in the form of [x,y,z] or " +
        "\"[x, y, z]\" or \"[x,y,z]\", where x, y, z are non-negative numbers."
    )
)
@click.option(
    "--max-grade",
    "-m",
    type=click.FloatRange(min=0),
    help=(
        "The maximum grade. If max-grade and passing-grade are not given, " +
        "it is set by default to 10. If only the passing-grade is given, " +
        "then it is set to double that of passing-grade."
    )
)
@click.option(
    "--passing-grade",
    "-p",
    type=click.FloatRange(min=0),
    help=(
        "The passing threshold grade. If passing-grade and max-grade are " +
        "not given, it is set by default to 5. If only the max-grade is " +
        "given, it is set to half of the max-grade."
    )
)
@click.option(
    "--personal-grade",
    "-pg",
    default=0,
    type=click.FloatRange(min=0),
    help=(
        "The grade that you scored. Giving this arguement will calculate " +
        "the percentage of grades that the given grade is higher than, in " +
        "relation to all the grades and to the passing grades. We consider " +
        "that the given grade is one of the grades in the grades list."
    )
)
def cli(file_grades, grades_list, max_grade, passing_grade, personal_grade):
    """
    A tool that shows useful statistics and generates a report about a set of
    given grades.

    Here are some examples:

    1. grades-report -l [40,80,75,60,90] -m 100 -p 60

    2. grades-report -l "[4, 8, 7.5, 6, 9]"

    3. grades-report -f /home/grades.csv ,

    You can find the source code at https://github.com/KAUTH/grades-report.
    """
    user_input = parse_user_input(
        file_grades, grades_list, max_grade, passing_grade, personal_grade
    )

    cli_output(user_input)


if __name__ == "__main__":
    cli()

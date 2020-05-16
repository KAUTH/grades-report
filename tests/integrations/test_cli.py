#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

# from click.testing import CliRunner

# from grades_report.cli import cli_output


# def test_cli_output():
#     grades_list = "[1,2,3,5,9]"

#     runner = CliRunner()
#     result = runner.invoke(cli_output, ["-l", grades_list])

#     expected_result = (
#         "/# Graded: 5\n/# Passed: 2\n/# Failed: 3\nArithmetic Mean of " +
#         "PASSING GRADES: 7.0\nArithmetic Mean of TOTAL GRADES: 4.0"
#     )

#     assert expected_result == result.output

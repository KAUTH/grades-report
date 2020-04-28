#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""

from grades_report.stats import mean_grade


def test_mean_grade():
    parsed_list = [2, 4, 6, 8]
    passing_grade = 5

    assert mean_grade(parsed_list, passing_grade, True) == 5
    assert mean_grade(parsed_list, passing_grade, False) == 7

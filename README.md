[![Build Status](https://github.com/KAUTH/grades-report/workflows/Python%20tests/badge.svg)](https://github.com/KAUTH/grades-report/actions?query=workflow%3A%22Python+tests%22)
[![codecov](https://codecov.io/gh/KAUTH/grades-report/branch/master/graph/badge.svg)](https://codecov.io/gh/KAUTH/grades-report)
[![pypi](https://img.shields.io/pypi/v/grades-report.svg)](https://pypi.python.org/pypi/grades-report)
[![GitHub license](https://img.shields.io/github/license/KAUTH/grades-report)](https://github.com/KAUTH/grades-report/blob/master/LICENSE)

# grades-report 📝

Get info and stats about grades

*grades-report* is a Command Line Interface (CLI) tool that shows useful statistics and generates a report about a set of given grades, e.g., from school, university, etc.

# Features

The report displays:

* The **number** of individuals that were **graded**, that **passed** and that **failed**

* The **arithmetic mean** of the **passing grades** (taking into account only grades that are over the passing threshold) and of the **total grades** (taking into account all the grades that are provided)

* The **standard deviation** of the **passing grades** (taking into account only grades that are over the passing threshold) and of the **total grades** (taking into account all the grades that are provided)

* The **maximum grade** from all the given grades

* The **minimum grade** of the **passing grades** (taking into account only grades that are over the passing threshold) and of the **total grades** (taking into account all the grades that are provided)

* The **percentage of the grades you have scored above** from the **total grades** (taking into account all the grades that are provided) and of the **passing grades** (taking into account only grades that are over the passing threshold)

* The **distribution** of all the grades (split into 10 equally sized and non-overlapping bins)

Example report (CLI output):

```
# Graded: 4
# Passed: 4
# Failed: 0

-----------------------------------------------------

Arithmetic Mean of PASSING GRADES: 7.0
Arithmetic Mean of TOTAL GRADES: 7.0

Standard Deviation of PASSING GRADES: 1.8257418583505538
Standard Deviation of TOTAL GRADES: 1.8257418583505538

Max TOTAL GRADE: 9.0
Min PASSING GRADE: 5.0 & Min TOTAL GRADE: 5.0

-----------------------------------------------------

Your grade: 6.0
You scored above 25.0% of all the grades.
You scored above 25.0% of the passing grades.

-----------------------------------------------------

GRADE       TOTAL
[0.0-1.0)      0
[1.0-2.0)      0
[2.0-3.0)      0
[3.0-4.0)      0
[4.0-5.0)      0
[5.0-6.0)      1
[6.0-7.0)      1
[7.0-8.0)      0
[8.0-9.0)      1
[9.0-10.0]     1
```

# Example usage

* To learn how to use the CLI tool just type: 

```grades-report --help```

* Creates a report for the following list of grades: 40, 80, 75, 60, 90, with the maximum grade being 100 and the passing threshold being 60 (if no arguments are given the defaults are 10 and 5 respectively):

 ```grades-report -l [40,80,75,60,90] -m 100 -p 60```

* Creates a report for the following list of grades: 4, 8, 7.5, 6, 9, with your personal grade being 8 (by default the perfect score is considered to be 10 and the passing grade 5):

```grades-report -l "[4, 8, 7.5, 6, 9]" -pg 8```

* Creates a report for the grades given in the file grades.csv, with the "," character used as a delimiter (for the path in Windows make sure to use double backslashes, \\\\, or a single forward slash, /.)

```grades-report -f /home/grades.csv ,```

# Installation

```pip install grades-report```

# Contributing

* You can always submit a PR if you want to suggest improvements or fix issues.

* Check out the open issues at https://github.com/KAUTH/grades-report/issues.

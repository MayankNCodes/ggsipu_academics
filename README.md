# ggsipu_academics

[![PyPI version](https://img.shields.io/pypi/v/ggsipu-academics.svg)](https://pypi.org/project/ggsipu-academics/)
[![Python Versions](https://img.shields.io/pypi/pyversions/ggsipu-academics.svg)](https://pypi.org/project/ggsipu-academics/)
[![License](https://img.shields.io/github/license/MayankNCodes/ggsipu_academics.svg)](https://github.com/<your-username>/ggsipu_academics/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/ggsipu-academics)](https://pepy.tech/project/ggsipu-academics)
-----

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [CLI Usage](#CLI-Usage)
- [Python-Usage](#Python-Usage)
- [License](#license)

## Overview

### ggsipu-academics 🎓

A Python Library and CLI tool for academic calculations for  
**Guru Gobind Singh Indraprastha University (GGSIPU)** students.

## Installation

```console
pip install ggsipu-academics
```
## CLI-Usage

```bash
ggsipu grade 85
ggsipu gradepoint 72
ggsipu sgpa --mode marks
ggsipu cgpa --mode sgpa
```
## Python-Usage

The following functions can be used to calculate the Semester Grade Point Average (SGPA) and Cumulative Grade Point Average (CGPA).

## Calculate SGPA

Calculate the Semester Grade Point Average (SGPA) of a student/individual studying in IPU.

## SGPAFromMarks

Calculate the SGPA from marks.

##### Parameters:
- **subjects (List[Tuple[int, int]])**: A list of tuples where each tuple contains the credits and marks obtained in a subject.
- **roundPrecision (int, optional)**: The number of decimal places to round the SGPA to. Default is 2.

##### Returns:
```float```: The calculated SGPA.

##### Raises:
```ValueError```: If the total credits are zero.

### Example:
    >>> from ggsipu_academics import Calculate
    >>> subjects = [(4, 80), (4, 70), (3, 90)]
    >>> Calculate.SGPAFromMarks(subjects)
    7.8

## SGPAFromGradePoint

Calculate the SGPA from grade points.

##### Parameters:
- **subjects (List[Tuple[int, float]])**: A list of tuples where each tuple contains the credits and grade point of a subject.
- **roundPrecision (int, optional)**: The number of decimal places to round the SGPA to. Default is 2.

##### Returns:
```float```: The calculated SGPA.

##### Raises:
```ValueError```: If the total credits are zero.

### Example:
```python
    >>> from ggsipu_academics import Calculate
    >>> subjects = [(4, 8.5), (4, 7.5), (3, 9.0)]
    >>> Calculate.SGPAFromGradePoint(subjects)
    8.33
```

## Calculate CGPA

Calculate the Cumulative Grade Point Average (CGPA) of a student/individual studying in IPU.

## CGPAFromSemesterMarks

Calculate the CGPA from semester marks.

##### Parameters:
- **semesters (List[List[Tuple[int, int]]])**: A list of lists where each list contains the credits and marks obtained in a subject for a semester.  
- **roundPrecision (int, optional)**: The number of decimal places to round the CGPA to. Default is 2.

##### Returns:
```float```: The calculated CGPA.

##### Raises:
```ValueError```: If the total credits are zero.

### Example:
```python
    >>> from ggsipu_academics import Calculate
    >>> semesters = [[(4, 80), (4, 70), (3, 90)], [(4, 85), (4, 75), (3, 95)]]
    >>> Calculate.CGPAFromSemesterMarks(semesters)
    8.42
```

## CGPAFromSemesterSGPA

Calculate the CGPA from semester GPAs.

##### Parameters:  
- **semesters (List)**: A list of semester GPAs.  
- **roundPrecision (int, optional)**: The number of decimal places to round the CGPA to. Default is 2.

##### Returns:
```float```: The calculated CGPA.

##### Raises:
```ValueError```: If the total credits are zero.

#### Example:
```python
    >>> from ggsipu_academics import Calculate
    >>> semesters = [7.8, 8.42]
    >>> Calculate.CGPAFromSemesterSGPA(semesters)
    8.1
```

## Example

```python
from ggsipu_academics import Calculate

print("Grade:", Calculate.Grade(85, roundPrecision=3)) # Output: Grade: A
print("Grade Point:", Calculate.GradePoint(85, roundPrecision=3)) # Output: Grade Point: 8.0
print("SGPA From Marks:", Calculate.SGPAFromMarks([(4, 85), (4, 75)], roundPrecision=3)) # Output: SGPA From Marks: 7.50
print("SGPA From Grade Point:", Calculate.SGPAFromGradePoint([(4, 7), (4, 8)], roundPrecision=3)) # Output: SGPA From Grade Point: 7.75
print("CGPA From Semester Marks:", Calculate.CGPAFromSemesterMarks([[(4, 7), (4, 8)], [(4, 8), (4, 9)]], roundPrecision=3)) # Output: CGPA From Semester Marks: 8.33
print("CGPA From Semester SGPA:", Calculate.CGPAFromSemesterSGPA([7.75, 8.5, 9.0], roundPrecision=3)) # Output: CGPA From Semester SGPA: 8.58
```


## License

`ggsipu-academics` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

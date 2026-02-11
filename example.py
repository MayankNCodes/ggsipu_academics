# pip install ggsipu-academics
from ggsipu_academics import Grade, GradePoint, SGPAFromMarks, SGPAFromGradePoint, CGPAFromSemesterMarks, CGPAFromSemesterSGPA,

print("Grade:", Grade(85)) # Output: Grade: A
print("Grade Point:", GradePoint(85)) # Output: Grade Point: 8.0
print("SGPA From Marks:", SGPAFromMarks([(4, 85), (4, 75)], roundPrecision=3)) # Output: SGPA From Marks: 7.50
print("SGPA From Grade Point:", SGPAFromGradePoint([(4, 7), (4, 8)], roundPrecision=3)) # Output: SGPA From Grade Point: 7.75
print("CGPA From Semester Marks:", CGPAFromSemesterMarks([[(4, 7), (4, 8)], [(4, 8), (4, 9)]], roundPrecision=3)) # Output: CGPA From Semester Marks: 8.33
print("CGPA From Semester SGPA:", CGPAFromSemesterSGPA([7.75, 8.5, 9.0], roundPrecision=3)) # Output: CGPA From Semester SGPA: 8.58

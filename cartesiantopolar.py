# Write a program to convert Cartesian coordinates into polar coordinates.

# cartesian coordinates: i and j
# so if r = ai + bj, |r| = sqrt(a^2 + b^2)
# polar coordinates are in the form (r, theta) and cartesian coordinates are in (a,b)
# theta = arctan(b / a)

import math as m

a = int(input("Enter value for a for the vector ai+bj:\n"))
b = int(input("Enter value for b for the vector ai+bj:\n"))

modR = m.sqrt(a**2 + b**2)
theta = m.atan(b / a)

polarCord = [modR, theta]
print(polarCord)

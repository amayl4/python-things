# Write a program to convert Cartesian coordinates into polar coordinates.

# cartesian coordinates: i and j
# so if r = ai + bj, |r| = sqrt(a^2 + b^2)
# polar coordinates are in the form (r, theta) and cartesian coordinates are in (a,b)
# theta = arctan(b / a)

import math as m

π = m.pi

a = int(input("Enter value for a for the vector ai+bj:\n"))
b = int(input("Enter value for b for the vector ai+bj:\n"))

modR = m.sqrt(a**2 + b**2)
theta = m.atan(abs(b/a))

if a < 0:
    theta = π - theta

if b < 0:
    theta = 2*π - theta

if a < 0 and b < 0:
    theta = π + theta

polarCord = [modR, theta]
print(polarCord)


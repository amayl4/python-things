# Write a program to convert Cartesian coordinates into polar coordinates.

# cartesian coordinates: i and j
# so if r = ai + bj, |r| = sqrt(a^2 + b^2)
# polar coordinates are in the form (r, theta) and cartesian coordinates are in (a,b)
# theta = arctan(b / a)

import math as m

i = [
    1,
    0
]
j = [
    0,
    1
]

a = int(input("Enter value for a:\n"))
b = int(input("Enter value for b:\n"))

cartesian = a*i + b*j
print(cartesian)

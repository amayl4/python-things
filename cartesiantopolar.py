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

# chatgpt's solution:
import math

def cartesian_to_polar(x, y):
    # Calculate the radius (r)
    r = math.sqrt(x**2 + y**2)
    
    # Calculate the angle (θ) in radians
    theta = math.atan2(y, x)
    
    # Convert angle from radians to degrees
    theta_degrees = math.degrees(theta)
    
    # Ensure theta is in the range [0, 360)
    if theta_degrees < 0:
        theta_degrees += 360
    
    return r, theta_degrees

# Example usage
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

r, theta = cartesian_to_polar(x, y)

print("Polar coordinates (r, θ):", r, "units,", theta, "degrees")




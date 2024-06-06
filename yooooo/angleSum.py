'''
Write a program to get the value of an angle in degrees as an input and finds out whether
the sum of sine or cosine of this angle is 1 or not.
'''
import math as m

θ = int(input("Enter angle in degrees:\n")) # Enter the angle
π = m.pi

# Convert angle from degrees to radians
ϕ = θ * (π / 180)

if m.sin(ϕ) + m.cos(ϕ) == 1:
    print("Sum is 1")
else:
    print("Sum is not 1")

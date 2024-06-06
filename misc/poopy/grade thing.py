'''
100 -> A*
80 -> A
70 -> B
60 -> C
50 -> D
...
10 -> F
0 -> U
'''

rawMark = int(input("Enter the raw mark: "))

def grade(rawMark):
    if rawMark <= 100 and rawMark >= 80:
        print("You got an A*")
    elif rawMark <= 80 and rawMark >= 70:
        print("You got an A")
    elif rawMark <= 10:
        print("You failed")

grade(rawMark)
'''
100 -> 9
80 -> 8
70 -> 7
60 -> 6
50 -> 5
...
10 -> 1
0 -> U
'''

rawMark = int(input("Enter your raw mark: \n"))

if rawMark <= 100 and rawMark >= 80:
    print("Grade 9")
elif rawMark <= 80 and rawMark >= 70:
    print("Grade 8")
elif rawMark <= 70 and rawMark >= 60:
    print("Grade 7")
elif rawMark == 0:
    print("You failed")

match rawMark:
    case "hello":
        print(100)
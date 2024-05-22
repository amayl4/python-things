'''
The marks obtained by a student in 8 different subjects are input through the
keyboard. Write a program to find the total marks and percentage marks
obtained by each student. Assume that the maximum marks that can be
obtained by a student in each subject is 100.
'''

# 1. input the subject marks
# 2. find the total of the marks
# 3. return the total marks out of 800
# 4. find the percentage by dividing by 800 then multiplying by 100

# enter all the marks
total = 0
for i in range(0,7):
    total += int(input("Enter the marks for a subject: "))
print(total)

# finding percentage
percentage = (total / 8)
print(percentage)
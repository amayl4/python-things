'''
Write a pseudocode algorithm that asks a user for a password. They are allowed three
attempts to type the correct password, which is “Tues1212”.
If they type the correct password, output “Password accepted”, otherwise output “Password
rejected”.
'''

password = "Tues1212"
user_input = input("Enter the password: \n")
n = 0

if user_input == password:
    print("Password accepted")
else:
    print("Password rejected")
    n += 1
    input("Enter the password: \n")

while n > 3:
    print("Maximum attempts used")

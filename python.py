user = input("Enter a value: ")
if user.isnumeric():
    print(" User input is a number.")
elif user.isalpha():
    print("User input is an alphabet.")
else:
    print("userinput is not number or alphabet.")
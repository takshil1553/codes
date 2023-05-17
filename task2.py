def ch (input_string):
    numeric = 0
    special = 0
    alphabet = 0
    
    for char in input_string:
        if char.isnumeric():
            numeric += 1
        elif char.isalpha():
            alphabet += 1
        else:
            special += 1

    return numeric,special,alphabet

input_string = input("Enter a string: ")
numeric,special,alphabet = ch (input_string)

print("number:", numeric)
print("alphabet:", alphabet)
print("special characters:",special)
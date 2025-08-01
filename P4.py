#...4.	Write a script that Count all letters, digits, and special symbols
# from a given string. inputString = "P@#yn26at^&i5ve"

inputString = "P@#yn26at^&i5ve9@"

count_lt = 0
count_dgt = 0
count_smbl = 0

for char in inputString:
    if char.isalpha():
        count_lt += 1
    elif char.isdigit():
        count_dgt += 1
    else:
        count_smbl += 1

print("Letters= ",count_lt)
print("Digits= ",count_dgt)
print("Special Symbols= ", count_smbl)

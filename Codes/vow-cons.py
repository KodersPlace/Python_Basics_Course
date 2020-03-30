string = input("Enter a string: ")

vow = 0
con = 0

# in

for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vow = vow + 1
    else:
        con += 1

print(f"String's length is {len(string)}")
print(f"Vowels are {vow}")
print(f"Consonants are {con}")
string = "Pakistan"
#         01234567
#         87654321       (negative)

# indexing
print(string[2])   # "k"

# negative indexing
print(string[-2])  # "a"

# for loops
for i in range(0, len(string)):
    print(string[i], end="")

# reverse for loop
for i in range(9, 1, -1):
    print(i)

# steps
for i in range(0, 11, 2):
    print(i)
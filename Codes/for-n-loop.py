# atom
# VS code
# pycharm

# for loops (nested)
'''
for i in range(5):  # 0,1,2,3,4

    for j in range(3): # 0, 1, 2

        print(f"i={i}, j={j}")
'''

students = [
    ["Hasham", 18, True, "Male", 6.0],
    ["Maaz", 21, True, "Male", 5.6],
    ["Midha", 19, True, "Female", 5.8],
]

for student in students:
    for data in student:
        print(data, end=", ")
    print()
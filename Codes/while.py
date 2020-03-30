# list
# string
# range

# i = 5
# while i <= 15:
#     print(i)
#     i += 2

# break
# continue

health = 10
run = True

while run:
    health = health - 1
    if health == 3:
        continue
    if health == 0:
        break
    print(f"Player running!! HP {health}")

print("Game end!")
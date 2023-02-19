# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

coordinates = []

for i in position:
  loc = int(i)
  coordinates.append(loc)

rows = int(coordinates[1]) - 1
columns = int(coordinates[0]) - 1

map[rows].pop()

map[rows].insert(columns, "X")


print(f"{row1}\n{row2}\n{row3}")

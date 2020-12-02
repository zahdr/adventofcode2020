import csv

input = list(csv.reader(open('input')))

## Part 1
correctPasswords = 0

for i in input:
    counter = 0

    data = i[0].split()
    amount = data[0].split("-")

    for j in data[2]:
        if j == data[1][0]:
            counter += 1

    if (counter >= int(amount[0])) and (counter <= int(amount[1])):
        correctPasswords += 1

print("Part 1:", correctPasswords)


## Part 2
correctPasswords = 0

for i in input:
    data = i[0].split()
    position = data[0].split("-")

    if (data[2][int(position[0])-1] == data[1][0]) is not (data[2][int(position[1])-1] == data[1][0]):
        correctPasswords += 1

print("Part 2:", correctPasswords)
    



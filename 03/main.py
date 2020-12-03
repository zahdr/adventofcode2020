import csv

input = list(csv.reader(open('input')))

## Part 1
trees = 0
cur_col = 0
cur_row = 0
max_col = len(input[0][0])
max_row = len(input)-1

while cur_row < max_row:
    cur_col += 3
    cur_row += 1
    if cur_col > max_col-1:
        cur_col = cur_col - max_col
    if input[cur_row][0][cur_col] == "#":    
        trees += 1

print("Part 1:",  trees)


## Part 2
steps = [[1,1], [3,1], [5,1], [7,1], [1,2]]
trees = []
mul_trees = 1
max_col = len(input[0][0])
max_row = len(input)-1

for move in steps:
    cur_trees = 0
    cur_col = 0
    cur_row = 0
    while cur_row < max_row:
        cur_col += move[0]
        cur_row += move[1]
        if cur_col > max_col-1:
            cur_col = cur_col - max_col
        if input[cur_row][0][cur_col] == "#":    
            cur_trees += 1
    trees.append(cur_trees)

for t in trees:
    mul_trees = mul_trees * t

print("Part 2:",  trees, mul_trees)
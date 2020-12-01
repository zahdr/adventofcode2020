import csv

input = list(csv.reader(open('input')))

print([int(i[0])*int(j[0])*int(k[0]) for i in input for j in input for k in input if int(i[0])+int(j[0])+int(k[0])==2020])

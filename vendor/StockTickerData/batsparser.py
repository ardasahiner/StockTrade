import csv

with open('bats_symbols.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    lis = []
    for row in reader:
        lis.append(row['Symbols'])

f = open('batslist.js', 'w')
s = str(lis)
f.write("module.exports = ")
f.write(s)
f.write(";")

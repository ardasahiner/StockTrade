import csv

with open('NASDAQ.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dict = {}
    for row in reader:
        dict[row['Name']] = row['Symbol']

with open('NYSE.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Name']] = row['Symbol']

with open('AMEX.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Name']] = row['Symbol']


f = open('reversestockdict.js', 'w')
s = str(dict)
f.write(s)

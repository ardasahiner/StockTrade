import csv

with open('AMEX.csv') as csvfile:
    dict = {}
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Symbol']] = 'AMEX'

with open('NASDAQ.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Symbol']] = 'NASDAQ'

with open('NYSE.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Symbol']] = 'NYSE'

f = open('stockdictexchange.js', 'w')
s = str(dict)
f.write(s)

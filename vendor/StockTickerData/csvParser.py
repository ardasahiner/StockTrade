import csv

with open('NASDAQ.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dict = {}
    for row in reader:
        dict[row['Symbol']] = row['Name']

with open('NYSE.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Symbol']] = row['Name']

with open('AMEX.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Symbol']] = row['Name']

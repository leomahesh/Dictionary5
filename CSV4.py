import csv
person = [['SN', 'Person', 'DOB'],
[1, 'John', '18/1/1997'],
[2, 'Marie','19/2/1998'],
[3, 'Simon','20/3/1999']]

csv.register_dialect('myDialect',quoting=csv.QUOTE_ALL)

with open('person.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)
f.close()
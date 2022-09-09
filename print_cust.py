import csv

infile = open('customers.csv', 'r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile) #skips first line

for record in csvfile:
    
    print('CustomerID:', record[0])
    print('CustFName:', record[1])
    print('CustLName:', record[2])
    print('City:', record[3])
    print('Country:', record[4])
    print('Phone:', record[5])

    input()




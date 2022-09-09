import csv

infile = open('employeepay.csv' , 'r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)

for record in csvfile:
    # setting records
    ID = record [0]
    EmpFName = record [1]
    EmpLName = record [2]
    Salary = record [3]
    Bonus = record[4]
    TotalPay = str(int(record[3]) + (int(record[3]) * float(record[4])))
    # print statements 
    print(format('ID:', '20') + ID)
    print(format('EmpFName: ', '20') + EmpFName)
    print(format('EmpLName: ', '20') + EmpLName)
    print(format('Salary:' , '20') + Salary)
    print(format('Bonus: ', '20') + Bonus)
    print(format ('Total Pay: ', '20' ) + TotalPay)
    input()
    
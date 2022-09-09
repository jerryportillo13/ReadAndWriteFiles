import csv

def main (): 
    infile = open('customers.csv', 'r')
    csvfile = csv.reader(infile, delimiter=',')
    outfile = open('customer_country.csv', 'w')


    for line in csvfile:
        outfile.write(format((line[1]), '20'))
        outfile.write(format((line[2]), '20'))
        outfile.write((line[4]) + '\t\n')
    
    infile.close()
    outfile.close()

main()





#months = ('January' = 1, 'February' =2 , 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
#days = ('')

def main():

    import csv
    infile = open('steps.csv', 'r').readlines()
    csvfile = csv.reader(infile, delimiter = ',')
    next (csvfile)
    write = csv.write(outfile, delimiter = ',')
    outfile = open('avg_steps.csv', 'w')

    sum = 0 #sum of steps 
    jan = 31
    for line in infile:
        if infile[0] == 1:
            sum += float(line)
    average = sum / jan
    
    writer.writerow(average)

main()

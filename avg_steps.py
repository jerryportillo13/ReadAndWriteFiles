import csv
import calendar

avgmonth = {}

with open('steps.csv') as file:
    filereader = csv.reader(file, delimiter = ',')
    count = 0

    for line in filereader: 
        if count == 0:
            count += 1
            continue
        else:
            NameOfMonth = calendar.month_name[int(line[0])]
            if int(line[0]) not in avgmonth.keys():
                avgmonth[int(line[0])] = [int (line[1])]
            else:
                avgmonth[int(line[0])].append(int(line[1]))

with open('avg_steps.csv', 'w') as avgsteps:
    avgstepswriter = csv.writer(avgsteps, delimiter = ',')
    avgstepswriter.writerow(['Month' '\tSteps'])
    month = list(avgmonth.keys())
    month.sort()

    for x in month:
        avgstepswriter.writerow([calendar.month_name[x], sum(avgmonth[x])/len(avgmonth[x])])
        #i tried to round off the number but couldnt figure out how to 

file.close()
avgsteps.close()

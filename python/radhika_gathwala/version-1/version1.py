import csv
from collections import defaultdict

inputFile = open('input.v1.csv')
inputReader = list(csv.reader(inputFile))
inputData = {}


for line in inputReader[1:]:
    if line[5] not in inputData:
        amt = line[1].replace('($','').replace('$','').replace(',','').replace(')','')
        if '(' in line[1]:
            inputData[line[5]] = (-1)* float(amt)
        else:
            inputData[line[5]] = float(amt)
    else:
        amt = line[1].replace('($','').replace('$','').replace(',','').replace(')','')
        if '(' in line[1]:
            inputData[line[5]] -= float(amt)
        else:
            inputData[line[5]] += float(amt)

for i,k in inputData.items():
    if k < 0:
        inputData[i] = '($' + str(-1*k) + ')'
    else:
        inputData[i] = '$' + str(k)
    print(i, ': ', k)


csvFileObj = open("v1.output-radhika.csv",'w')
csvWriter = csv.writer(csvFileObj)
csvWriter.writerow(inputData.keys())
csvWriter.writerow(inputData.values())
csvFileObj.close()

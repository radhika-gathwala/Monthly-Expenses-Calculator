import csv
from collections import defaultdict

inputFile = open('input.v2.csv')
inputReader = list(csv.reader(inputFile))
vendors= {}
categoryTotal= {}

for line in inputReader[1:]:
    vendor = line[2].replace('-',' ').replace(',',' ').lower()
    vendor = vendor.split()
    if vendor[0] not in vendors:
        vendors[vendor[0]] = line[5]
    else:
        if line[5] not in vendors[vendor[0]]:
            vendors[vendor[0]] += line[5]
      
for line in inputReader[1:]:
    category = line[5]
    vendor = line[2].replace('-',' ').replace(',',' ').lower()
    vendor = vendor.split()
    if category == '':
        category = vendors[vendor[0]]
    else:
        category = line[5]
    if category not in categoryTotal:
        amt = line[1].replace('($','').replace('$','').replace(',','').replace(')','')
        line[1].split()
        if '(' in line[1]:
            if category == '':
                category = 'WARNING-NO-CATEGORY'
            categoryTotal[category] = (-1)* float(amt)
        else:    
            if category == '':
                category = 'WARNING-NO-CATEGORY'
            categoryTotal[category] = float(amt)
    else:
        amt = line[1].replace('($','').replace('$','').replace(',','').replace(')','')
        if '(' in line[1]:
            categoryTotal[category] -= float(amt)
        else:
            categoryTotal[category] += float(amt)
            
for j,m in vendors.items():
   print(j, ': ', m)
    
for i,k in categoryTotal.items():
    if k < 0:
        categoryTotal[i] = '($' + str(-1*k) + ')'
    else:
        categoryTotal[i] = '$' + str(k)
    print(i, ': ', k)

csvFileObj = open("v2.output-radhika.csv",'w')
csvWriter = csv.writer(csvFileObj)
csvWriter.writerow(categoryTotal.keys())
csvWriter.writerow(categoryTotal.values())
csvFileObj.close()

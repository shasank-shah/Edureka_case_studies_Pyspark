import csv
import re
from Customer import Customer

_string = 'Mr. Shasank Shah'
_period = _string.find('.')
print(type(_period))
_title = slice(0, 2)
print(_string[_title])

'''

_title = set()
with open('FairDealCustomerData.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        
        if line_count == 0:            
            line_count += 1
        else:
            unique_jobs.add(row[1])
            age.append(row[0])
        
        xx = row[1]
        print(xx)
        r1 = re.findall(r"^\w+", xx)
        print(r1)
'''
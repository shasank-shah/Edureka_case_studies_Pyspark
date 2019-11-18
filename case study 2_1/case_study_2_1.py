import csv

unique_jobs = []
with open('bank-data.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    file_column = []
    for row in csv_reader:
        if line_count == 0:
            file_column = row
            line_count += 1
        else:
            unique_jobs.append(row[1])

unique_jobs = set(unique_jobs)
profession = input("Enter the profession name: ")
if profession in unique_jobs:
    print("The client is eligible to be approached for marketing campaign")
else:
    print("The client is not eligible to be approached for marketing campaign")
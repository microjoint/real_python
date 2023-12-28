import csv

with open('employee_birthday.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print( row )
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["month"]}')

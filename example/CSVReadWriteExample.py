#https://realpython.com/python-csv/
import csv

def readCSV():
    with open('employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
def writeCSV():
    with open('employee_birthday.txt', mode='w') as employee_file: #เขียนทับ
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar ='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
        employee_writer.writerow(['Ratta Chindasilpa', 'IoT engineer', 'August'])
        employee_writer.writerow(['Suchanuch Klongvicha', 'Digital marketing', 'August'])

writeCSV()




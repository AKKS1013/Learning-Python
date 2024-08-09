import csv

def find_longest_serving_employee(filename):
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    longest_serving_employee = None

    for row in reader:
      years_of_service = int(row['yearsOfService'])
      if longest_serving_employee is None or years_of_service > longest_serving_employee[1]:
        longest_serving_employee = (row['employeeName'], years_of_service)

  return longest_serving_employee

def find_highest_paid_employee(filename):
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    highest_paid_employee = None

    for row in reader:
      salary = int(row['salary'])
      if highest_paid_employee is None or salary > highest_paid_employee[1]:
        highest_paid_employee = (row['employeeName'], salary)

  return highest_paid_employee

if __name__ == '__main__':
  filename = 'file.csv'
  longest_serving = find_longest_serving_employee(filename)
  highest_paid = find_highest_paid_employee(filename)
  print(f"The longest serving employee is {longest_serving[0]} with {longest_serving[1]} years of service.")
  print(f"The highest paid employee is {highest_paid[0]} with a salary of {highest_paid[1]}.")

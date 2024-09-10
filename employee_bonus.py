
import csv

emp_file = open('employee_data.csv', 'r')

emp_dat = csv.reader(emp_file)

next(emp_dat)

for rec in emp_dat:

    Total_Salary = float(rec[3]) * (1+float(rec[7]))

    Total_Salary = int(Total_Salary)

    print(f"{rec[1]},{' '+'$' +' '+ str(Total_Salary)}")

  

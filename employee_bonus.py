
import csv

emp_file = open('employee_data.csv', 'r')

emp_dat = csv.reader(emp_file)

next(emp_dat)

for rec in emp_dat:
    Salary = float((rec[3]))
    Bonus = float(rec[3]) * float((rec[7]))
    Total_Salary = Salary + Bonus

    print(f"Name : {rec[1]}")

    print(f"Salary: $ {Salary:,.2f}")

    print(f"Bonus:  $ {Bonus:,.2f}")

    print(f"Pay:    $ {Total_Salary:,.2f} \n")

    #print("Bonus:"+'$' +' '+ str(f"{Bonus:,.2f)}"))
    #print("Pay:" + '$' +' '+ str(f"{Total_Salary:,.2f)} \n "))

  

from tabulate import tabulate

import EmployeeClass as l

import PayrollDeductionClass as t

employee = l.Employee("Jimmy Smith","58475","Information Systems","Developer","$6,800.00")

#Option 1
#print(" Name       ID Number       Department        Job Title       Monthly Salary      \n",
#employee.get_name(),employee.get_IDnumber(),employee.get_department(),employee.get_jobtitle(),employee.get_salary())

#Option 2
employee_table = [["Name","ID Number","Department","Job Title","Monthly Salary"],[employee.get_name(),employee.get_IDnumber(),employee.get_department(),employee.get_jobtitle(),employee.get_salary()]]
print(tabulate(employee_table))



#########################################


transactions = float(input("How many transactions do you have? "))

count = 0

#description_table=[]
#date_table=[]
charge_table=[]
#employeeID_table=[]


while count < transactions:
    description = input("What is the description of the transaction? ")
    date = input("What date did the transaction happen? ")
    charge = float(input("What was the transaction charge? "))
    employeeID = input("What is the employee ID? ")
    #description_table.append(description)
    #date_table.append(date)
    charge_table.append(charge)
    #employeeID_table.append(employeeID)
    count +=1



payroll = t.PayrollTransactions(description,date,charge,employeeID)
transaction_table = [["Description","Date","Charge","EmployeeID"],[payroll.get_description(),payroll.get_date(),payroll.get_charge(),payroll.get_employeeID()]]



print(tabulate(transaction_table))

Total = sum(charge_table)



#####################################################


print("Employee Pay")
print("Name: ", employee.get_name())
print("ID Number: ",employee.get_IDnumber())
print("Department: ",employee.get_department())
print("Gross Pay: ",employee.get_salary())
salary = (employee.get_salary().replace("$","").replace(",",""))
salary = float(salary)
print("Net Pay: $", salary - Total)




from tabulate import tabulate

import EmployeeClass as l

import PayrollDeductionClass as t

employee = l.Employee("Jimmy Smith","58475","Information Systems","Developer","$6,800.00")

employee_table = [["Name","ID Number","Department","Job Title","Monthly Salary"],[employee.get_name(),employee.get_IDnumber(),employee.get_department(),employee.get_jobtitle(),employee.get_salary()]]
print(tabulate(employee_table))


payroll_1 = t.PayrollTransactions("food court","8/14/2022",22.50,"39119") 

payroll_2 = t.PayrollTransactions("gift contribution","8/12/2022",25.00,"58475")

payroll_3 = t.PayrollTransactions("food court","8/17/2022",15.25,"21547")

payroll_4 = t.PayrollTransactions("vending machine","8/22/2022",3.00,"58475")

payroll_5 = t.PayrollTransactions("vanding machine","8/5/2022",2.75,"58475")

payroll_table = [["Description","Date","Charge","EmployeeID"],[payroll_1.get_description(),payroll_1.get_date(),payroll_1.get_charge(),payroll_1.get_employeeID()],[payroll_2.get_description(),payroll_2.get_date(),payroll_2.get_charge(),payroll_2.get_employeeID()],[payroll_3.get_description(),payroll_3.get_date(),payroll_3.get_charge(),payroll_3.get_employeeID()],[payroll_4.get_description(),payroll_4.get_date(),payroll_4.get_charge(),payroll_4.get_employeeID()],[payroll_5.get_description(),payroll_5.get_date(),payroll_5.get_charge(),payroll_5.get_employeeID()]]


print(tabulate(payroll_table))

if employee.get_IDnumber() == payroll_1.get_employeeID() or payroll_2.get_employeeID() or payroll_3.get_employeeID() or payroll_4.get_employeeID() or payroll_5.get_employeeID():
    charge_table=[payroll_2.get_charge(),payroll_4.get_charge(),payroll_5.get_charge()]
    Total = sum(charge_table)



print("*** Employee Pay ***")
print("Name: ", employee.get_name())
print("ID Number: ",employee.get_IDnumber())
print("Department: ",employee.get_department())
print("Gross Pay: ",employee.get_salary())
salary = (employee.get_salary().replace("$","").replace(",",""))
salary = float(salary)
print("Net Pay: $", "{:,}".format(salary - Total))

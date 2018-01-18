# payroll
name = str(input("Enter Name: "))
hours = int(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: "))
CPF = int(input("Enter CPF contribution rate(%): "))

Gross = hours * rate
Contribution = ((CPF/100) * Gross)
Net = Gross - Contribution 

print("Payroll statement for {0} ".format(name))
print("Number of hours worked in week: {0}".format(hours))
print("Hourly pay rate: {0}".format(rate))
print("Gross pay = ${0:.2f}".format(Gross))
print("CPF contribution at {0}% = ${1:.2f}" .format(CPF,Contribution))
print("Net pay = ${0:.2f}".format(Net))



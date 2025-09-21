# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = float(.065) * salary
federalTax= float(.28) * salary
dependentDeduction = (float(.025) * salary) * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
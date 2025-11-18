"""write a progra that takes salary as input. Using conditional Statements, calculate the final tax rate based on following rules
   if salary < 30000 -> 5%
   if salary 30000 - 70000 ->15%
   if salary >70000 -> 25%
   """

salary = int(input("Enter the Salary amount :"))

if (salary< 30000):
    tax = salary * 0.05
    print ("Tax to pay : ", tax)

elif(salary > 30000 and salary < 70000):
    tax = salary * 0.15
    print ("Tax to pay : ", tax)
else:
    tax = salary * 0.25
    print ("Tax to pay : ", tax)

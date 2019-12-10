#---------------------------------
# Kenny Coons
# OOP Assignment
# December 12/ 19
#---------------------------------
# ----------Imports-------------
import time, random
#----------Clsses----------------
class Employer:
    raise_amt = 5.8
    def __init__(self, first, middle, last, pay):
        self.first = first
        self.middle = middle
        self.last = last
        self.email = first + '.' + last + '@lskysd.ca'
        self.pay = pay

    def full_name(self):
        return'{} {}'.format(self.first, self.middle, self.last)
   
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amt)
    
        
class Employee(Employer):
    raise_amt = 2.01
    def __init__(self, first, middle, last, pay):
        super().__init__(first, middle,  last, pay)
        self.pay = pay
    

        
    
employer = Employer ("Eugene", "Harold", "Krabs", 1000000000)
employee = Employee ("Squidward", "Q", "Tentacles", 89000)

print (employee.full_name)
print (employer.full_name)

print (employer.email)
print(employee.email)

print (employee.first, 'hates spongebob')
print (employer.first, 'loves spongebob')
print (employee.pay)
employee.apply_raise()
print(employee.pay)
print(employer.pay)
employer.apply_raise()
print(employer.pay)



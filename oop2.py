class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last =last
        self.pay = pay
        self.email = first +'.' + last + '@company.com'

        Employee.num_of_emp +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Huy','Le',60000)

emp1.raise_amount = 1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
print()

print(Employee.num_of_emp)
"""
print(Employee.__dict__)
print()
print(emp1.__dict__)
print()

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)"""

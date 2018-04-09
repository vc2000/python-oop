class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last =last
        self.pay = pay
        self.email = first +'.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Huy','Le',60000)

print(emp1.email)
#print('{} {}'.format(emp1.first, emp1.last))
print(emp1.fullname())

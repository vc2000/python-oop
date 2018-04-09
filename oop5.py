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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Huy','Le',200)


print(len(emp1))
#print(emp1 + emp2)



"""
##########special method##################

#repr and str can be call out directly
print(repr(emp1))
print(str(emp1))
print()
print(emp1.__repr__())
print(emp1.__str__())
print()

#same as the math
print(1+2)
print(int.__add__(1,2))
print()

print('a'+'b')
print(str.__add__('a','b'))

###########################################################
"""

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

    #classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #classmethod
    def from_string(cls, emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first, last, pay)

    #static method
    #don"t pass instant or class
    #like function
    #have relation with class
    def is_workday(day):
        #5 = Saturday
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        return True


emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Huy','Le',60000)

# static method
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


"""
Employee.set_raise_amount(Employee,1.05)
#emp1.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)"""
########################################################
"""emp3_str = 'Joe-Doe-70000'
emp4_str = 'Steve-Smith-30000'
emp5_str = 'Jance-Doe-90000' """

"""
first , last , pay = emp3_str.split('-')
emp3 = Employee(first, last, pay)

print(emp3.email)
print(emp3.pay)

#class classmethod
emp3 = Employee.from_string(Employee,emp3_str)
emp4 = Employee.from_string(Employee,emp4_str)
print(emp3.email)
print(emp4.pay)"""

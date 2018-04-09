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

#subclass, inheritance
class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay,prog_lang):
        pass
        #maintain the Employee class __init__
        #either way, pass Employee or use "super"
        #Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp1 = Employee('Corey','Schafer',50000)

#Developer is a subclass, inheritance

dev1 = Developer('Venus','Chau',100000,'Python')
dev2= Developer('Huy','Le',60000, 'Java')
print(dev1.email)
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print(dev1.prog_lang)

#print(help(Developer))

mgr1 = Manager('Annie','Cheung', 50000000000, [dev1])
print(mgr1.email)
mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.print_emps()

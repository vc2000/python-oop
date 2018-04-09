class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last):
        self.first = first
        self.last =last
    # add @property
    # access fuction - email like an attrbute
    # call out , don't need ()
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)


    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    #name ----- Annie Cheung fullname
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None





emp2 = Employee('Venus','Chau')
emp2.fullname = ('Annie Cheung')


print(emp2.first)
print(emp2.email)
print(emp2.fullname)
print()
del emp2.fullname
########################################################3

"""
emp1 = Employee('Huy','Le')

emp1.first = 'Jim'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
"""

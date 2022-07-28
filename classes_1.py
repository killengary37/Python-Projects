

class Employee:  #first class defining employee, defines first name
                 #last name, pay and email

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self)
        return '{} {}'.format(self.first, self.last)

    
class Developer(Employee):  #1st child class is developer, base pay and language
    base_pay = 75000.00
    pro_lang = 'python'

class Manager(Employee):    #2nd child class manager, which department and how many employees under them
    department = 'engineering'
    num_employees = ' '
    



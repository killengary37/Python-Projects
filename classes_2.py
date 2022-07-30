

class Employee:  #first class defining employee, defines first name
                 #last name, pay and email

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
class Developer(Employee):  #1st child class is developer, base pay and language

    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay)
        self.pro_lang = pro_lang

        
        

class Manager(Employee):    #2nd child class manager, which department and how many employees under them

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):   #adds employee to managers employees
        if emp in self.employees:
            self.employees.append(emp)

    def remove_emp(self):    #remove employee from list of employees of the manager
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self): #function to print out the employees of the manager
        for emp in self.employees:
            print('-->', emp.fullname())

            

dev_1 = Developer('Gary', 'Killen', 60000, 'Python')
dev_2 = Developer('Obi', 'Kenobi', 75000, 'Java')

mgr_1 = Manager('Beatrice', 'Jones', 100000, [dev_2])

mgr_1.print_emps()
   


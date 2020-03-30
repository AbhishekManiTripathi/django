class Employee:

    raise_ratio = 1.05

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        #self.email = fname + '.' + lname + '@email.com' # see below
        self.pay = int(pay)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.fname, self.lname)   
        # by using property decorator we can use this  method to define an attribue

    def raise_pay(self): # normal method here we pass the instance only
        self.pay = self.pay * self.raise_ratio  # simply raise_ration will not work, you will have to acces either with a class variable or instance if you wil 
        # here if you will wirte Employee.raise_ratio then you wont be able to raise the pay by instance variable.
    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last    
    
    @fullname.deleter
    def fullname(self):
        # first, last = name.split(' ')
        print ('In deleter of full name')
        self.fname = None
        self.lname = None    


    @classmethod
    def from_string(cls, emp_str):    # in class method a class is passed, here we are using this as an alternative constructor
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)


    @staticmethod
    def is_weekday(day):   # In static method, we dont pass either instance or class
        pass    
        
    def __repr__(self):  # dunder metohds
        return "('{} {} {}')".format(self.fname, self.lname, self.pay)

    def __str__(self):
        return '{} {}'.format(self.fname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())       
       




# emp1 = Employee('Anshu', 'pandey', 10000)

# print(emp1.pay)
# emp1.raise_pay()
# print('\n\nAfter increment', emp1.pay)
# emp2_str = 'abhishek-mani-5000'
# emp2 = Employee.from_string(emp2_str)
# print (emp2.pay)
# emp2.raise_pay()
# print(emp2.pay)
# print('Now incrementing it by 10 percent')
# emp2.raise_ratio = 1.10
# emp2.raise_pay()
# print(emp2.pay)

class Devloper(Employee):

    raise_ratio = 1.10  # devlopers having more hike then the egular employees

    def __init__(self, fname, lname, pay, lang): # dunder method
        super().__init__(fname, lname, pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, emp_list = None):
        super().__init__(fname, lname, pay)
        if emp_list:
            self.emp_list = emp_list
        else :
            self.emp_list = []    

    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def remove_emp(self, emp):
         if emp  in self.emp_list:
            self.emp_list.remove(emp)

    def print_emps(self):
        for emp in self.emp_list:
            print('Employee ----> ' + emp.fname + ' ' + emp.lname)

    

emp1 = Employee('Gaurvish', 'Gupta', '2500')
#emp2 = Devloper('Keyur', 'Soni', '2600', 'pytohn')
emp3 = Employee('furkaan', 'raja', '3500')

# mgr1 = Manager('Abhishek Mani', 'Tripathi', '30000', [emp1, emp2])

# mgr1.add_emp(emp3)

# mgr1.print_emps()          
# print(emp1)

# print(int.__add__(1,2))    # int oject add function 
# print(str.__add__('1', '2')) # string object add function

# now suppose you want to calculate salaries of all emps by adding the emps only ad not their salary then what ? 

# print(emp1 + emp3)  # by using dunder method to get their total salary
# print(1+2)
# print(len(emp1))



### decorators , getters , setters and deleters


print(emp1.fname)
print(emp1.email)
print(emp1.fullname)
print('#'*10 + ' problem below is even after setting first name to abhishek gaurvish is geeting printed here ' + '#'*10)
emp1.fname = 'abhishek'

emp1.fullname = 'mani abhishek' #3) will gove error can't se attribute   # but this will work after setter

print(emp1.fname)
print(emp1.email)  # 2)remove @ property and uncomment self.email in __init_ of employee to see the changes
print(emp1.fullname)

del(emp1.fullname)

# a possible soulution is that we can make an email method , but other people using the same code wiil have to change how the objects are getting instantiated 
# there fore we will use setters and getters 1) by using @ propertyop

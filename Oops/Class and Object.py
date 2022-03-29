# class Employee:
#     fname = "Steve"
#     lname = "Jobs"
#
# emp1 = Employee()
# emp2 = Employee()
#
# ######## Accessing class variables with objects ##########
# print(emp1.fname)
# print(emp2.lname)
#
#
# ######## Accessing class variables with classname ##########
# print(Employee.lname)


######## Creating the object variables in class #############
# class Employee:
#     fname = "Shiva"
#     lname = "Satya"
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname


# emp1 = Employee("Mark","Antony")
# emp2 = Employee("Mahendra","Singh")
#
# # ######## Accessing class variables with object ##########
# print(emp1.fname)
# print(emp2.lname)
#
# # ######## Accessing class variables with classname ##########
# print(Employee.fname)
# print(Employee.lname)

# print(Employee.__dict__)
# print(emp1.__dict__)

# class Calculator:
#     a = 10
#     b = 20
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def multi(self):
#         return self.a*self.b
#     def div(self):
#         return self.a%self.b
#
#
# calci = Calculator()
# ###### calling functions using object #########
# print(calci.add())
# print(calci.sub())
# print(calci.multi())
# print(calci.div())
#
#
# # ######## Calling Functions using Class ##########
# print(Calculator.add(calci))
# print(Calculator.sub(calci))
# print(Calculator.multi(calci))
# print(Calculator.div(calci))

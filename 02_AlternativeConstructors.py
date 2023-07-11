# Class Methods As Alternative Constructors

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))
    
    
# Arslan = Employee("Arslan", 255, "Instructor")
# Umar = Employee("Umar", 455, "Student")
# # Ibrahim = Employee.from_dash("Ibrahim-480-Student")

# # print(Ibrahim.no_of_leaves)
# # Ibrahim.change_leaves(34)
# print(Arslan.no_of_leaves)

Aun = Employee.from_dash("Aun-580-Student")
print(Aun.printdetails())

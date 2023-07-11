class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        print(f"The name of Employee is {self.name} salary is {self.salary} and role is {self.role}")
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    


Arslan = Employee("Arslan", 500000, "Admin")
Umar = Employee("Umar", 200000, "Manager")

Arslan.printdetails()
Umar.printdetails()

Arslan.change_leaves(4)
print(Arslan.no_of_leaves)
print(Umar.no_of_leaves)

Umar.change_leaves(5)
print(Arslan.no_of_leaves)
print(Umar.no_of_leaves)
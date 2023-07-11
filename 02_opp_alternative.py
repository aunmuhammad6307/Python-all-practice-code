
class Employee:
    leaves = 2
    def __init__(self, name, age, role):
        self.fname = name
        self.myage = age
        self.role = role

    def display(self):
        print(f"The perosn name is {self.fname} & his age is {self.myage} his deprt is {self.role}")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.leaves = newleaves
    
    @classmethod
    def from_str(cls, string):
        # lst = string.split("-")
        # return cls(lst[0], lst[1], lst[2])
        return cls(*string.split("-"))


Adnan = Employee.from_str("Adnan-21-soldier")
Adnan.display()
print(Adnan.leaves)
# arslan = Employee("Arslan", 23, "Admin")
# arslan.display()
# print(arslan.leaves)
# arslan.change_leaves(35)
# print(arslan.leaves)
# print(Employee.leaves)


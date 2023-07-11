# class MyClass:
#     def __init__(self, name, age, deprt):
#         self.name = name
#         self.age = age
#         self.deprt = deprt
    
#     def display(self):
#         print(f"The name of person is {self.name}\nThe age of {self.name} is {self.age}\nThe depart of {self.name} is {self.deprt}")


# p1 = MyClass("Arslan", 23, "Computer Science")
# print(p1.name)
# print(p1.age)
# print(p1.deprt)
# p1.display()
# p1.age = 25
# p1.display()
# del p1.age
# p1.display()



class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname 
    
    def display(self):
        print(f"The name of person is {self.fname} {self.lname}")
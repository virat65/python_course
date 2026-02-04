# class student:
#   branch = "CSE"
#   def __init__(self,naam,umar):
#     self.name = naam
#     self.age = umar
# s1 = student("ram",88)
# print(s1.name,s1.age)




class Student:
    name = "anonymous"   # class attribute
    branch = "CSE"       # class attribute

    def __init__(self, naam=None, umar=None):
        if naam is not None:
            self.name = naam       # override class attribute
        self.age = umar            # object attribute


# Creating objects
s1 = Student()                # uses class attribute "anonymous"
s2 = Student("Raj", 18)       # overrides name and sets age

print(s1.name, s1.age)     # anonymous CSE
print(s2.name, s2.age)        # Raj 18

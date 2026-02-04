# def game_Win():
#  pass

# print("hello")




# def my_function(person):
#   print("Name:", person["nameee"])
#   print("Age:", person["ageee"])

# my_person = {"nameee": "Emil", "ageee": 25}
# my_function(my_person)



# def my_function(x, y,z,s):
#    sum = x+y +z+s
#    print(sum)
#    return "i'm good"


# print(my_function(5, 3,9,9))
# my_function = "i'm good"


# class car:
#     @staticmethod # decorator to mark greet as a static method
#     def greet(height):
#      print("Hello user",height)


#     def hello(self,name,age):
#        self.naam= name
#        self.umar =age
#        print("my name is ",self.naam ,self.umar)
# p1 = car()
# p1.hello("Ram",77)
# p1.greet(88)



# class Employee:
#   @property
#   def name(self):
#     return self.ename




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  x = 8
  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()

class Student(Person):
  def greet(self):
    print("helllo")
  def printname(self):
    print("hello ram")
  x = 6
ram = Student("Mike", "Olsen")
ram.printname()

ram.greet()


p1 = Student("Raj",99)
print(p1.x)

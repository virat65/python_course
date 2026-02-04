class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()


# multiple inheritace
class Father:
    def skill(self):
        print("Father: Coding")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()   # Father method runs (due to order)

# 3. Multilevel Inheritance

# Grandparent → Parent → Child
class A:
    def showA(self):
        print("A class")

class B(A):
    def showB(self):
        print("B class")

class C(B):
    def showC(self):
        print("C class")

obj = C()
obj.showA()
obj.showB()
obj.showC()



# Hierarchical Inheritance

# One parent → multiple children.
# class Animal:
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()

d.eat()
c.eat()



# 5. Hybrid Inheritance

# Combination of more than one type.

class A:
    def msgA(self):
        print("A")

class B(A):
    def msgB(self):
        print("B")

class C(A):
    def msgC(self):
        print("C")

class D(B, C):
    def msgD(self):
        print("D")

obj = D()
obj.msgA()

# ⭐ Inheritance With super() (Important)

# super() is used to call parent class methods.
class Parent:
    def show(self):
        print("Hello from Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Hello from Child")

c = Child()
c.show()

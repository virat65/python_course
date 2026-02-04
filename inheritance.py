class Parent:
    def _init_(self,fname,lname):
        print("Parent constructor")
        print(fname,lname)

class Child(Parent):
    def _init_(self,fname,lname):
        super()._init_()   # calls Parent constructor
        print("Child constructor")
        print(fname,lname)
c = Child()
c._init_("ram","sign")

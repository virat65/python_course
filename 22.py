class A:
  def show(self):
    print("By A")

class B(A):
  def show(self):
    super().show()
    print("By b")
class C(B):
  def show(self):
    pass
    super().show()
    print("By C")
x = C()
x.show()

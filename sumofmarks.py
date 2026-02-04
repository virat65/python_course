class student:
  def __init__(self,name,marks):
    self.naam = name
    self.number = marks
  @staticmethod
  def hello():
      print("hello user ")

  def avg(self):
    sum = 0
    for val in self.number:
      sum +=val
    print(f"hi {self.naam} your avg is {sum/4}")
s1 = student("ram",[10,20,30,40])
s1.avg()
s1.hello()

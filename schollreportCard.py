record= {}
for i in range(0,3):
  name = input("enter your name ")
  marks = int(input("Enter your marks "))
  record.update({f"{name}":f"{marks}"})
print(record)
marks_list= record.values()
marks_list1=list(marks_list)
# marks_list.sort()
marks_list1.sort()
length = len(marks_list1)
print(marks_list1)

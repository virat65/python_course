# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))
# ss = { }


# new = {}
# for i in range(4):
#   name = input("enter your name ")
#   lang = input("enter your fav language ")
#   new.update({name:lang})
# print(new)



# -->Unique Numbers Finder
# 👉 Write a program to take a list of numbers and print only the unique numbers using a set.
# Example:
# Input → [1, 2, 2, 3, 4, 4]
# Output → {1, 2, 3, 4}

# blank_list= []
# for i in range(0,5):
#   item = int(input("Enter number "))
#   blank_list.append(item)
# print(blank_list)
# newset = set(blank_list)
# print(newset)



# Common Elements
# 👉 Find the common elements between two lists using sets.
# Example:
# [1, 2, 3, 4] and [3, 4, 5, 6] → Output: {3, 4}

list1 = [1, 2, 3, 4,4,5,5]
list2= [3,4,5,6]
newlist = []
for i in range(0,len(list1)):
  if(list1[i]==list1[i-1]):
      list_item= list1[i]
      print("duplicate element")
  else:
      list_item= list1[i]
      newlist.append(list1[i])
print(newlist)


# set1= set(list1)
# set2 = set(list2)
# set3 = set1.difference(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)
# list3 = list(set4)
# print(list3)

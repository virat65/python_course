# user = {
#   "ram": {
#     "age": 18,
#     "ismarried": True,

#   },
#     "raj": {
#     "age": 18,
#     "ismarried": False,

#   }, "raj": {
#     "age": 18,
#     "ismarried": 12,

#   },
# }
# # print(user["raj"]["ismarried"])
# # user["raj"]["ismarried"] = True
# # print(user["raj"]["ismarried"])
# # print(user)

# print(3==6)
# print(1==True)
# print(0==False)
# print(False*6)

# print(len(user))



# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")
# thisset.add("orafdsnge")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)



# --->
# thisset = {"apple", "banana", "cherry"}

# thisset.remove("bananee")

# print(thisset)


# ---->
# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)


# #
# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)
# # ---

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)

# # --
# # thisset = {"apple", "banana", "cherry"}

# # del thisset

# # print(thisset)

# # --




# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# # set1.update(set2)
# # print(set1)


# set3 = set1.union(set2)
# print(set1)
# print(set2)
# print(set3)

# # ---->

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# set1.update(set2,set3)
# myset = set1.union(set2, set3, set4)
# print(set1,"hellooo")
# print(myset)


# # --/
# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)


# # /-->

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)


# # --->
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)

# # --->

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)



# #  /



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)


# # /---
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)


# ///--->
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)


# # / --->
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set2.difference(set1)

# print(set3)


# # -->
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)



# # /---->

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set2.difference_update(set1)
# print(set1)

# print(set2)


# />


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


# --->
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

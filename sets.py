user = {"Ram","raj","Raju","sita","sita","sita"}
print(user)
print(type(user))



print(len(user))


# thisset = dict({
# "apple":"hello", "banana":"hiii", "cherry":"hhiii"
# }) # note the double round-brackets
# print(type(thisset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(type(thisset))



thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
else:
  print("done")
print("bananadfasdf" not in thisset)
# print("banana" in thisset)

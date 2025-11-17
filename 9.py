thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x = thisdict["modell"]
# y= thisdict.get("modell")
# print(y)
# print(x)
x = thisdict.items()
print(x)
for x ,y in thisdict.items():
  print(x ,":",y)
# for i in range(1,5):
#   print(i)
# else:
#   print("hello")

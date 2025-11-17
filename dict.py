user = {
  "name":"ram",
  "age":34,
  "ismaried" : True,
"ismaried" : False,
  "marks":[12,15,18]
}
print("name" not in user)
print("name" in user)
# usersanme = dict["name":"shaym ","age":66]
number = int(66.88)
new = {""}
print(user)
print(user["name"])
print(user.keys())
print(user.values())
print(user.get("name"))

print(len(user))
print(type(user))
print(type(number))
print(user.items())
print(type(new))
user["name"]="raj"
print(user)
user.update({
"number":877697,
"naame":"rajesh"
})
print(user)
print(user.pop("name"))
print(user)
print(user.popitem())
print(user)
# del user
print(user)
user.clear()
print(user)


# name = "ram"
name = ["ram","shaym","raj"]
# name = 12345
for j  in name:
  print(j)

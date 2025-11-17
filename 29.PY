# name= "abcdefghijklm"
# print(name)
# newname = name[1:3]
# print(newname)
# newname2 = name[1]
# print(newname2)
# newname1 = name[:3]
# print(newname1)
# newname3 = name[1:]
# print(newname3)
# newname4= name[0:7:3]
# print(newname4)
# print(name[1])
# print(name[-4:-2])


# funtions
str= "amazzzing"

print(len(str))
print(str.endswith("he"))
print(str.endswith("ing"))
print(str.startswith("on"))
print(str.startswith("amz"))
print(str.startswith("amaz"))
print(str.count("z"))
print(str.__contains__("amaaa"))

print(str.__contains__("ama"))
print(str.__contains__("azg"))
print(str.index("z"))
print(str.find("z"))
print("hello")
print(str.capitalize())
print(str.upper())
newstr= "HELLOKA"
print(newstr.lower())
print(newstr.replace("L","h"))

string = "Hello, World!"

index = string.find("l")
new_char = 'a'
new_string = string[:index] + new_char + string[index+1:]
print(new_string)  # Output: "Helloa, World!"
# string[:index] == 0,1 hea


newstr5 = "hello dosto"
print(newstr5.replace(" ","         "))

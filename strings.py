name = "ramanand"
print(name.capitalize()) #capitalize the first character only
print(name.startswith("ra"))
print(name.endswith("d"))
print(name.startswith("ara"))
print(name.endswith("da"))
newname = name[0:3]
print(newname)
newname2 = name[3]
print(newname2)

print(name[-7:-1]) # -7 : -1 means from -7 to -1 that is amanana
print(name[:4]) # :4 means from string till index 4
print(name[1:]) #1: means 1 to length

# string skiping
a = "01234567890"
b = a[0:5:2] # first a[0:5] gives = 01234 then start from 1 give  2nd charcter every time
print(b)


print("hi my name is ramanand i'm 21 years old,      i live \tin mohali punjab")
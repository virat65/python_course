# row = 5
# for i in range(0,row):
#   for j in range(0,i):
#     print( chr(65+j),end="")
#   print()


print("new pattern")

# row = 5
# for i in range(1,row):
#   for j in range(0,i):
#     print( chr(64+i),end="")
#   print()


row = 8
for i in range(1,row):
  for j in range(0,i):
    print( chr(64+(i*i)),end="")
  print()

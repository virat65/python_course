# length = 5
# for row in range(length):
#   for column in range(row):
#     print(column,end="")
#   print()



length = 3
for row in range(1,length+1):

   for column in range(length-row , -1, -1):
    print(row,end="")

   print()

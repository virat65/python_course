# simple traingle

num= int(input("enter your number"))
# num = 9
print("here your triangle with row", num)
for i in range(1,num +1):
  for j  in range(1,i+1):
     print("*",end="")
  print("")
print("new triangel from herer"
"")


# inverse traiangle
# for i in range(9,1,-1):
#  for j in range(1,i):
#    print("*",end="")
#  print("")
# print("new triangel from herer")

#mirror triangle
# for i in range(9,1,-1):
#  for j in range(i,1,-1):
#    print("*",end="")
#  print("")



# triangle 4
# for i in range(9,1,-1):
#  for j in range(i,1,-1):
#    print(" ",end="")
#  print("" ,end="*")



# #  Pyramid Pattern
# print("  Pyramid Pattern")
# rows = 5
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))


# # Mirror Right-Angled Triangle
# print("Mirror Right-Angled Triangle")
# rows = 5
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * i)


# # Inverse Mirror Triangle
# print("Inverse Mirror Triangle")
# rows = 5
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) + "*" * i)


# # Mirror Right-Angled Triangle
# print("Mirror Right-Angled Triangle")

# rows = 5  # Number of rows in the triangle

# for i in range(1, rows + 1):
#     # Print spaces before stars
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for k in range(i):
#         print("*", end="")

#     # Move to next line after each row
#     print()



# # Inverse Mirror Right-Angled Triangle
# print("\nInverse Mirror Right-Angled Triangle")

# rows = 5  # Number of rows in the triangle

# for i in range(rows, 0, -1):
#     # Print spaces before stars
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for k in range(i):
#         print("*", end="")

#     # Move to next line after each row
#     print()




# n = 5
# for i in range(1, n+1):            # Loop for rows
#     for j in range(n-i):           # Loop for '#'
#         print("#", end="")
#     for k in range(2*i-1):         # Loop for '*'
#         print("*", end="")
#     print()



# abcd patter
# n = 5
# for i in range (99):
# #    num =  int(input("enter"))
#     print(i)
#     print(chr(65 + i))


# row = 10
# for i in range(1,row+1):
#     for j in range(1,i):
#         print(chr(64+j),end="")
#     print()

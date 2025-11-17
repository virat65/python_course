sorted_list= []
reverse_list= []
for i in range(1,6):
  numbers = int(input("Enter the number : "))
  sorted_list.append(numbers)
  print("done")
sorted_list.sort()
# print(reverse_list,"reverser")
# print(length ,"length")
print(sorted_list)

length = len(sorted_list) # 5
# sorted_list.sort(reverse=True)
# print(sorted_list)
for i in range (1,length+1):
    temp_var= sorted_list[length-i]
    print(temp_var,"temp")
    reverse_list.append(temp_var)
print(sorted_list,"sorted list")
print(reverse_list,"reverse_list")

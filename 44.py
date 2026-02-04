number = int(input("enter the number"))
arr = []
for i in range(number+1):
  arr.append(i)
print(arr)

ans=0
for x in range(len(arr)):
 ans= ans+arr[x]
print(ans)

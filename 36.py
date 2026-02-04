def details(**d):
  # print(d.items())
  for v ,k in d.items():
    print(v,": ", k)

details(name="ram",age=66,gender="male",)


def add(*d):
  sum= 0
  for num in d:
    sum= sum+num
  return sum
print(add(7,8))

# def num(**dd):
#   print(type(dd))
#   print((dd))

# num(name="ram",age=77,gender="male")

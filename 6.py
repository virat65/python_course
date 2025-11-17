import random;
user={
    "name":"ram",
"age":19,
"ismarried":True,
"marks":[12,22,34,34]
}

# print(user.values())
# print(user["age"])
# for x in user:
#     print(x , " : " , user[x])
# print(user["name"])
# string = "ram is my best friend"
# if "ram" in string:
#     print(True)
# else:
#     print(False)

# for x in string:
#     print(x)
# print(user.values())
# for x in user.keys():
#     print(x)
# for x in user.values():
#     print(x)
# for x ,y in user.items():
#     print(x,y)
# print(user.items())


current_price = 90
open_market_price = current_price
print(current_price,"current price")
print(open_market_price ,"starting price")
for i in range(1,9):
    print(i," pm")
    marketchange = random.choice([-5,5,99,-8,3,-9,10,100])
    print(marketchange,"rs change")
    current_price = current_price+ (marketchange)
    print(current_price,"after change ")

    # print(open_market_price,"at_that_timerow_value")
    # print(current_price,"current price")
    print("--------------------")
if open_market_price>current_price:
         print("stock price decreased")
         print(open_market_price,"market open price")
         print(current_price,"current price ")
else:
        print(open_market_price,"market open price")
        print(current_price,"current price ")
        print("stock price increased")
# row = 5
# for i in range(1,row):
#     print("*"* i )

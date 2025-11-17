import random;
current_price = 100
open_market_price = current_price
print(current_price,"current price")
print(open_market_price ,"starting price")
for i in range(1,9):
    print(i," pm")
    marketchange = random.randint(-10,10)
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

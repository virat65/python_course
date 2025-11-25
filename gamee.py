import random
computer_enter = random.choice(["r","p","c"])
user_enter = input("Enter Your Choice (r/p/c): ")
gamedictionary = {
  1:"rock",
  2:"paper",
  3:"crissor"
}
reversegamedictionary ={
     "r":1,
     "p":2,
     "c":3
}
computer =reversegamedictionary[computer_enter]
user = reversegamedictionary[user_enter]
computerwin = "Computer wins"
userwin  = "user wins"
print(f"You choose {gamedictionary[reversegamedictionary[user_enter]]} and the computer choose {gamedictionary[reversegamedictionary[computer_enter]]}")
if(computer==user):
    print("Its a Draw")
else:
     if(computer==1 and user==2):
           print(userwin)
     elif computer==1 and user ==3:
          print(computerwin)
     elif computer==2 and user==1:
          print(computerwin)
     elif computer==2 and user==3:
          print(userwin)
     elif computer==3 and user==1:
          print(userwin)
     elif computer==3 and user==2:
          print(computerwin)
     else:
          print("Something Went wrong")

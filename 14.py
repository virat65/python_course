with open("hiscore.txt","r") as message:
  readMessage = message.read()
  print(readMessage)
if "donkey" in readMessage:
  print("bad words present")
  filterdmessage = readMessage.replace("donkey","####")
else:
    print("no bad words")
with open("hiscore.txt","w") as newmessage:
   newmessage.write(filterdmessage)
   print(newmessage)

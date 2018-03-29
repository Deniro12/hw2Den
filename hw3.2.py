ticket=input("Enter your ticket number: ")
if len(ticket)!=4:
   exit("Error")
if int(ticket) == 4576:
    print("You win!!!")
else: print("Lucky next time")
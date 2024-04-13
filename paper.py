import random
userchoice=int(input("enter your choice:rock=0.paper=1.scissor=2 :"))
computerchoice=random.randint(0,2)
print("computer choice :",computerchoice)
if computerchoice==userchoice:
    print("It's tight")
elif computerchoice>userchoice:
    print("you lose")
elif computerchoice<userchoice:
    print("you win")
elif computerchoice==0 and userchoice==2:
    print("you lose")
elif computerchoice==2 and userchoice==0:    
    print("you win")

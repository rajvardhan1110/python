import random

# snake=-1
# water=0
# gun=1


computer=random.choice([0,1,-1])

yourChoice=input("enter your choice: ")
yourDic={
    "s":-1,
    "w":0,
    "g":1
}

yourAns=yourDic[yourChoice]

reverseDic={
    -1:"snake",
    0:"water",
    1:"gun"
}

print(f"the computer's choice is {reverseDic[computer]} \nyour choice is {reverseDic[yourDic[yourChoice]]}")

if computer==yourAns:
    print("its Draw")
else:
    if (computer==1 and yourAns==-1):
        print("computer win...!")
    elif (computer==1 and yourAns==0):
        print("computer win...!")
    elif (computer==0 and yourAns==-1):
        print("computer win...!")
    elif (computer==0 and yourAns==1):
        print("you win...!")
    elif (computer==-1 and yourAns==1):
        print("you win...!")
    elif (computer==-1 and yourAns==0):
        print("you win...!")
    else:
        print("somthing wrong happen")
 
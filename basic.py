# def check(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")    

# n= int(input("enter a number "))
# check(n)

f=open("text.txt","w+")

f.write("RAJVARDHAN PATIL")

f.seek(0)

data=f.read()

f.close()

if data.find("RPATIL")!= -1:
    print("found")
else:
    print("not found")    






num=[]

for i in range(5):
    n=int(input("enter number: "))
    num.append(n)

sum=0

for i in range(len(num)):
    sum += num[i]

print(sum)

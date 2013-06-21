n=input()
a=raw_input()
k=0
mas=[]
mas=a.split()
for i in range(0,n):
    if int(mas[i])%2!=0:
        k+=1
print k

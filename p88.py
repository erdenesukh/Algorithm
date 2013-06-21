n=int(raw_input())
k=1
f=0
l=n%10
a=n
while a>10:
	a=a/10
	f=a
	k=k*10
print n-f*k-l+l*k+f


	


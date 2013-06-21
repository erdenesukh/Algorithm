x,y=raw_input().split()
if x>y:
	z=float(x)-float(y)
	print round(float(z),1)
else:
	z=float(y)-float(x)+1
	print round(float(z),1)


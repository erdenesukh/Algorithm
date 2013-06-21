x,y,z=raw_input().split()
a=float(x)+float(y)+float(z)
b=float(x)*float(y)*float(z)
if a>b:
	print round(float(a),1)
else:
	print round(float(b),1)

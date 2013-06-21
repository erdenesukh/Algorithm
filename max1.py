x,y,z=raw_input().split()
max=x
if float(y)>float(x):
	max=y
if float(z)>float(y):
	max=z
print round(float(max),1)


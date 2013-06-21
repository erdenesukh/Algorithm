import math
x,y,z=raw_input().split()
print round(float(y)+float(x)/(float(y)*float(y)+math.fabs(float(x)*float(x)/(float(y)+float(x)*float(x)*float(x)/3))),1)
b=1+math.tan(float(z)/2)*math.tan(float(z)/2)
print round(b,1)

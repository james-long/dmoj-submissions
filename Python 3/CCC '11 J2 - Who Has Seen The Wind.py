import sys,re;all_data=sys.stdin.read().split('\n')
a,t,h,m,printed=-1,1,int(all_data[0]),int(all_data[1]),False
while t<m:
     a=-6*t**4+h*t**3+2*t**2+t
     if a<=0:print("The balloon first touches ground at hour:\n%i"%t);printed=True;break
     t+=1
if not printed:print("The balloon does not touch ground in the given time.")
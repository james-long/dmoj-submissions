import sys;all_data=sys.stdin.read().split("\n")[1:-1]
for x in all_data:
     fac=[y for y in range(1,int(int(x)**0.5)+1) if int(x)%y==0]
     more=[int(x)/y for y in fac[1:]]
     final=set(fac+more)
     if sum(final)>int(x):print("%s is an abundant number."%x)
     elif sum(final)<int(x):print("%s is a deficient number."%x)
     else:print("%s is a perfect number."%x)
import sys;all_data=sys.stdin.read().split("\n")[1:-1]
for x in all_data:
     a,b,c=x.split()
     if int(a)*int(b)==int(c):print("POSSIBLE DOUBLE SIGMA")
     else:print("16 BIT S/W ONLY")
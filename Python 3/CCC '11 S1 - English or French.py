import sys;all_data=sys.stdin.read().split("\n")[1:-1]
t,s=0,0
for x in all_data:t+=x.count("T")+x.count("t");s+=x.count("S")+x.count("s")
if t>s:print("English")
else:print("French")
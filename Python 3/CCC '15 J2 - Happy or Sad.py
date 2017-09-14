import sys;all_data=sys.stdin.read().split("\n")
h,s=all_data[0].count(":-)"),all_data[0].count(":-(")
if h==s:
    if h==0:print("none")
    else:print("unsure")
elif h>s:print("happy")
else:print("sad")
import sys
all_data=sys.stdin.read().split('\n')
if int(all_data[0],16)+int(all_data[1],16)>1061109567:print("Yes")
else:print("No")
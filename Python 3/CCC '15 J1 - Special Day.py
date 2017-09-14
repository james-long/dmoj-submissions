import sys;all_data=sys.stdin.read().split("\n")
if int(all_data[0])<2:print("Before")
elif int(all_data[0])==2:
    if int(all_data[1])<18:print("Before")
    elif int(all_data[1])==18:print("Special")
    elif int(all_data[1])>18:print("After")
else:print("After")
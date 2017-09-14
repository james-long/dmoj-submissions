import sys
all_data=sys.stdin.read().split('\n')
if str(all_data[1])[-1:]=="e":
     print(str(all_data[0])+"-tu la "+str(all_data[1])+" ?")
elif str(all_data[1])[-1:]=="s":
     print(str(all_data[0])+"-tu les "+str(all_data[1])+" ?")
else:
     print(str(all_data[0])+"-tu le "+str(all_data[1])+" ?")
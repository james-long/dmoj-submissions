import sys
all_data=sys.stdin.read().split('\n')
num=all_data[0]
num=(num[:3]+num[4:7]+num[8:])
if int(num[0])+int(num[1])+int(num[2])==int(num[3])+int(num[4])+int(num[5])==int(num[6])+int(num[7])+int(num[8])+int(num[9]):print("Goony!")
else:print("Pick up the phone!")
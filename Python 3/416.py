import sys,re;all_data=sys.stdin.read().split("\n")
num,valid=re.sub(" ","",all_data[0]),["416","647","437"]
if len(num)!=10 or num[:3] not in valid:print("invalid")
else:
     if num[:3]=="416":print("valuable")
     else:print("valueless")
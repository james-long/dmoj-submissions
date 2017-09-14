import sys;all_data=sys.stdin.read().split("\n")
weight=int(all_data[0])
all_data=all_data[2:-1]
on=[]
for num,wei in enumerate(all_data):
     on.append(int(wei))
     if len(on)>4:on=on[1:]
     if sum(on)>weight:print(num);break
if sum(on)<=weight:print(len(all_data))
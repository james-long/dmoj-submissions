import sys;all_data=sys.stdin.read().split("\n");num=set()
for x in all_data[1].split():num.add(x)
print(len(num))
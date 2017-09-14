import sys;all_data=sys.stdin.read().split('\n')[1:-1]
while len(all_data)>0:a=min(int(x) for x in all_data);print(a);all_data.remove(str(a))
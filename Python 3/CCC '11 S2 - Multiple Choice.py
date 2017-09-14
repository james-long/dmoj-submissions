import sys;all_data=sys.stdin.read().split("\n")[1:-1]
ans,cor=all_data[:int(len(all_data)/2)],all_data[int(len(all_data)/2):]
right=[y for x,y in enumerate(ans) if y==cor[x]]
print(len(right))
import sys,itertools;all_data=sys.stdin.read().split("\n")
pie,ppl=int(all_data[0]),int(all_data[1])
if pie==ppl or ppl==1:print("1")
else:
    print(len([x for x in (itertools.product(range(1,pie+1),repeat=ppl)) if sum(x)==pie and sorted(x)==list(x)]))
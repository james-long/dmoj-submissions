import sys;all_data=sys.stdin.read().split("\n")[1:-1]
for sent in all_data:
     words=[x if len(x)!=4 else "****" for x in sent.split()]
     print(" ".join(words))
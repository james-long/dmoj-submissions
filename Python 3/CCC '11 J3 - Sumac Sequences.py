import sys,re;seq=[int(x) for x in sys.stdin.read().split('\n')[:-1]]
while seq[-1]<=seq[-2]:
     seq.append(abs(seq[-2]-seq[-1]))
print(len(seq))
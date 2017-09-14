import sys
all_data=sys.stdin.read().split("\n")
rec,a,b=all_data[0].split()
rec,a,b,tot=int(rec),int(a),int(b),0
for x in range(1,rec+1):
     if a<=int(all_data[x])*2<=b:
          tot+=1
print(tot)
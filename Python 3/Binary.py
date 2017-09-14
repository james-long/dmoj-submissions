import sys
all_data=sys.stdin.read().split("\n")
def binary(num):
     return bin(num)[2:]
for x in range(1,int(all_data[0])+1):
     a=binary(int(all_data[x]))
     if len(a)//4==0:
          print(a.zfill(4))
     elif len(a)%4==0:
          for y in range(len(a)%4,len(a),4):print(a[y:y+4],end=" ")
          print()
     else:
          print(a[:len(a)%4].zfill(4),end=" ")
          for y in range(len(a)%4,len(a),4):print(a[y:y+4],end=" ")
          print()
import sys
all_data=sys.stdin.read().split("\n")
lst1,lst2=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"],["2","3","4","5","6","7","8","9"]
def number(num):
     num=num.replace("-","")
     new=""
     for x in range(10):
          if 64<ord(num[x])<91:
               for y in range(8):
                    if num[x] in lst1[y]:new+=lst2[y];break                    
          else:new+=num[x]
     return new[:3]+"-"+new[3:6]+"-"+new[6:]
for x in range(1,int(all_data[0])+1):print(number(all_data[x]))
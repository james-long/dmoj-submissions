import sys,math
def getfactor(first,last,factors):
     goodnums=[]
     for x in range(first,last+1):
          factortotal=[x]
          if x%2!=0:
               for y in range(1,int(math.sqrt(x))+1,2):
                    if x%y==0 and not (y in factortotal):
                         factortotal.append(y)
                         factor2=x/y
                         if factor2 not in factortotal:
                              factortotal.append(factor2)
          else:     
               for y in range(1,int(math.sqrt(x))+1):
                    if x%y==0 and not (y in factortotal):
                         factortotal.append(y)
                         factor2=x/y
                         if factor2 not in factortotal:
                              factortotal.append(factor2)
          if len(factortotal)==factors:
               goodnums.append(x)
          factortotal[:]=[]
     return goodnums

all_data = sys.stdin.read().split('\n')
total=int(all_data[0])
for x in range(1,total+1):
     num=all_data[x].split(" ")
     factors=int(num[0])
     first=int(num[1])
     last=int(num[2])
     print(len(getfactor(first,last,factors)))
import sys
all_data=sys.stdin.read().split("\n")
def rhyme(num):
     a,b,c,d=all_data[num].split(" ")[-1].lower(),all_data[num+1].split(" ")[-1].lower(),all_data[num+2].split(" ")[-1].lower(),all_data[num+3].split(" ")[-1].lower()
     rhymelist=[a,b,c,d]
     for w in range(4):
          y=[]
          for x in "aeiou":
               y.append(rhymelist[w].rfind(x))
          z=max(y)
          if z>-1:
               rhymelist[w]=rhymelist[w][z:]
     if rhymelist[0]==rhymelist[1]==rhymelist[2]==rhymelist[3]:return "perfect"
     elif rhymelist[0]==rhymelist[1] and rhymelist[2]==rhymelist[3]:return "even"
     elif rhymelist[0]==rhymelist[2] and rhymelist[1]==rhymelist[3]:return "cross"
     elif rhymelist[0]==rhymelist[3] and rhymelist[1]==rhymelist[2]:return "shell"
     else:return "free"
for x in range(1,int(all_data[0])*4,4):print(rhyme(x))
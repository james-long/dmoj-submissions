import sys
all_data = sys.stdin.read().split('\n')
lst=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
for x in range(len(all_data)):
     if all_data[x]!="halt":
          sec=0
          for y in range(len(all_data[x])):
               for z in range(8):
                    if all_data[x][y:y+1] in lst[z].lower():
                         sec+=lst[z].lower().find(all_data[x][y:y+1])+1
                         if all_data[x][y+1:y+2] in lst[z].lower():
                              sec+=2

          if sec!=0:print(sec-2)
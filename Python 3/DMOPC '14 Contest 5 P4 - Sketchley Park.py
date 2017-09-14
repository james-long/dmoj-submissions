import sys
all_data=sys.stdin.read().split("\n")
word,yn=all_data[0],False
for x in range(2,int(all_data[1])+2):
     code,hh=all_data[x],[]
     for y in "HAILHYDRA":
          hh.append(code[ord(y)-65])
     hydra=""
     for x in hh:hydra+=x
     if hydra in word:
          newword=""
          for z in word:newword+=chr(code.find(z)+65)
          print(newword)
          yn=True
          break
if not yn:print("KeyNotFoundError")
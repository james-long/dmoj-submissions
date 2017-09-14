import sys,re
all_data=sys.stdin.read().split("\n")
keyword,words,move=all_data[0],re.sub("[^A-Z]","",all_data[1]),[]
for x in range(len(keyword)):move.append(ord(keyword[x])-65)
mcount,mmax=0,len(move)
for x in words:
     a=ord(x)+move[mcount]
     if a>90:a-=26
     print(chr(a),end="")
     mcount+=1
     if mcount==mmax:mcount=0
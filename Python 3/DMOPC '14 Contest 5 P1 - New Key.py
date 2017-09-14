import sys
all_data=sys.stdin.read().split("\n")
word,newword=all_data[0],""
for x in word:
     if x=="0":newword+="9" 
     elif 48<ord(x)<58:newword+=chr(ord(x)+16)
     elif 64<ord(x)<81:newword+=chr(ord(x)+9)
print(newword)
     
import sys
all_data = sys.stdin.read().split('\n')
p,k,word,alpha=3,int(all_data[0]),all_data[1],"ZYXWVUTSRQPONMLKJIHGFEDCBA"
for x in word:
     new=alpha.find(x)+p+k
     while new>25:
          new-=26
     print(alpha[new],end="")
     p+=3
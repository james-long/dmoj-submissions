import sys;all_data=sys.stdin.read().split("\n")
vowel=[97,101,105,111,117]
for let in all_data[0]:
    print(let,end="")
    if ord(let) not in vowel:
        a=min(((abs(y-ord(let)),x) for x,y in enumerate(vowel)))
        print(chr(vowel[a[1]]),end="")
        if let=="z":print("z",end="")
        else:
            letnum=ord(let)
            while True:
                letnum+=1
                if letnum not in vowel:
                    print(chr(letnum),end="");break
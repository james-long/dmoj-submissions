import sys;all_data=sys.stdin.read().split("\n")[1:-1]
clock,msglist=0,[]
friends=[]
for msg in all_data:
    x,y=msg.split()
    if x!="W" and int(y) not in friends:friends.append(int(y))
friends.sort()
for num,msg in enumerate(all_data[:-1]):
    if msg[0]!="W":
        msglist.append((msg,clock))
        if all_data[num+1][0]=="W":a,b=all_data[num+1].split();clock+=int(b)
        else:clock+=1
msglist.append((all_data[-1],clock))
for fri in friends:
    recieved=0
    reccount=0
    replied=0
    repcount=0
    total=0
    for msg in msglist:
        a,b=msg[0].split()
        if a=="R" and int(b)==fri:recieved+=msg[1];reccount+=1
        elif a=="S" and int(b)==fri:replied+=msg[1];repcount+=1
    if reccount>repcount:total=-1
    else:total=replied-recieved
    print("%i %i"%(fri,total))
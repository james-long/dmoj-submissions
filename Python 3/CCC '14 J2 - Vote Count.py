input()
votes=input()
while "A" in votes or "B" in votes:
    acount=0
    bcount=0
    while "A" in votes:
        afind=votes.find("A")
        votes=votes[:afind]+"@"+votes[afind+1:]
        acount+=1
    while "B" in votes:
        bfind=votes.find("B")
        votes=votes[:bfind]+"@"+votes[bfind+1:]
        bcount+=1
if acount>bcount:
    print("A")
elif bcount>acount:
    print("B")
else:
    print("Tie")
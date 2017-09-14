import sys; all_data = sys.stdin.read().split('\n')
q=int(all_data[0])
tot=int(all_data[1])
dmoja=[int(i) for i in all_data[2].split(" ")]
pega=[int(i) for i in all_data[3].split(" ")]
dmoj=sorted(dmoja,reverse=True)
peg=sorted(pega,reverse=True)
if q==1:
    ans=0
    for i in range(tot):
        ans+=max(dmoj[i],peg[i])
    print(ans)
else:
    ans=0
    for i in range(tot):
        if dmoj[0]>peg[0]:
            ans+=dmoj[0]
            peg.pop(len(peg)-1)
            dmoj.pop(0)            
        else:
            ans+=peg[0]
            dmoj.pop(len(dmoj)-1)
            peg.pop(0)
    print(ans)
import sys
all_data=sys.stdin.read().split("\n")
st=set()
for x in range(1,int(all_data[0])+1):
     if all_data[x] not in st:st.add(all_data[x])
print(len(st))
import sys
all_data = sys.stdin.read().split('\n')
words=["CU",":-)",":-(",";-)",":-P","(~.~)","TA","CCC","CUZ","TY","YW","TTYL"]
translations=["see you","I'm happy","I'm unhappy","wink","stick out my tongue","sleepy","totally awesome","Canadian Computing Competition","because","thank-you","you're welcome","talk to you later"]
for x in range(len(all_data)):
     if all_data[x] in words:
          print(translations[words.index(all_data[x])])
     else:
          print(all_data[x])
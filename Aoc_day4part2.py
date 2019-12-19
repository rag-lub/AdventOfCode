from collections import Counter

def dblseq(str1):
    c = Counter(str1)
    if 2 in c.values():
        return True
    return False

def incr(str1):
    for i in range(len(str1)-1):
        if int(str1[i]) > int(str1[i+1]):
            return False
    return True
#print(dblseq(str(136770)),incr(str(136889)))
ctr = 0
for i in range(136760,595730):
    if dblseq(str(i)):
        if incr(str(i)):
            ctr+=1
print(ctr)
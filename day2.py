# Anagram using Built in Methods
def Anagram(s,p):
    if len(s)!=len(p):
        return False
    return sorted(s)==sorted(p)
s="collection"
p="tieolcnclo"
result=Anagram(s,p)
print(result)

#2 Anagram without using methods
def Anagram(s,p):
    if len(s)!=len(p):
        return False
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in p:
        if i in dic:
            dic[i]-=1
        else:
            dic[i]=-1
    for i in dic.values():
        if i!=0:
            return False
    return True
s="collection"
p="tieolcnclo"

#3 Solving using counting list
def Anagram(s,p):
    if len(s)!=len(p):
        return False
    lt=[]*26
    for i in s:
        lt[ord(i)-97]+=1
    for i in p:
        lt[ord(i)-97]-=1
    for i in range(26):
        if lt[i]!=0:
            return False
    return True
s="collection"
p="tieolcnclo" 
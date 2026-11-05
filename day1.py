#Frequency Counting and Dictionary
def fun(s):
    n=len(s)
    for i in range(n):
        b=True
        for j in range(i):
            if s[i]==s[j]:
                b=False
                break
        if b:
            r=0
            for j in range(i,n):
                if s[i]==s[j]:
                    r+=1
            print(f"{s[i]} -> {r}")
s="programing"
fun(s)

#2
def fun1(n):
    dic={}
    for i in n:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in n:
        if dic[i]!=0:
            print(f"{i} -> {dic[i]}")
            dic[i]=0
n="python"
fun1(n)   

#3
def fun2(p):
    lt=[0]*26
    for i in p:
        lt[ord(i)-ord('a')]+=1
    for i in p:
        if lt[ord(i)-97]!=0:
            print(f"{i} -> {lt[ord(i)-97]}")
            lt[ord(i)-97]=0
p="algorithm"
fun2(p)


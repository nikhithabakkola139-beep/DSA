#Finding duplicate elements with without extra place
def duplicate(a):
    res=[]
    for i in a:
        i=abs(i)
        if a[i-1]<0:
            res+=[i]
        else:
            a[i-1]=-a[i-1]
    return res
a=[4,3,2,7,8,2,3,1]
s=duplicate(a)
print(s)

#2.Longest Palindrome Build
def palindrome(e):
    dic={}
    for i in e:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    count=0
    for i in dic.values():
        count+=i//2*2
        if count%2==0 and i%2==1:
            count+=1
    return count
e="abccccdd"
f=palindrome(e)
print(f)

        

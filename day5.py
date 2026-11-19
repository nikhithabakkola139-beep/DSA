#Two string Uncommon Elements
def Uncommon_str(s,p):
    lt=[0]*26
    for i in s:
        lt[ord(i)-97]=1
    for i in p:
        if lt[ord(i)-97]==1 or lt[ord(i)-97]==-1:
            lt[ord(i)-97]=-1
        else:
            lt[ord(i)-97]=2
    st=""
    for i in range(26):
        if (lt[i]==1 or lt[i]==2):
            st+=chr(i+97)
    return st
s="characters"
p="alphabets"
m=Uncommon_str(s,p)
print(m)

# A String Palindrome or Not with 2 pointer approch
def reverse(s):
    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
s="abcdef"
n=reverse(s)
print(n)
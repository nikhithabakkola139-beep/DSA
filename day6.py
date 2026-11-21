#Removing Duplicate Elements from the array with 2 pointer approch
def RemoveDuplicate(arr):
    n=len(arr)
    s=0
    for f in range(1,n):
        if arr[f-1]!=arr[f]:
            s+=1
            arr[s]==arr[f]
    return s+1
arr=[1,1,2,2,3,3,3,3,4,4]
d=RemoveDuplicate(arr)
print(d)


#Make Zeros at last of List
def Zero(a):
    n = len(a)
    s = 0
    for i in range(n):
        if a[i] != 0:
            a[s], a[i] = a[i], a[s]
            s += 1
    return a

a = [7, 0, 6, 0, 0, 1, 8, 0, 9]
h = Zero(a)
print(h)

#Pair with given sum 
def PairSum(x,k):
    st=set()
    for i in x:
        c=k-i
        if c in st:
            return c,i
        st.add(i)
    return False
x=[2,17,16,12,4,15]
k=27
g=PairSum(x,k)
print(g)


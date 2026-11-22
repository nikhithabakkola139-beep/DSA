#1.Merge 2 Lists with 2 pointer approch
# Merge 2 Lists with 2 pointer approach
def Merge(a, b):
    a.sort()
    b.sort()

    n = len(a)
    m = len(b)
    merge = []

    li = ri = 0

    while li < n and ri < m:
        if a[li] < b[ri]:
            merge.append(a[li])
            li += 1
        else:
            merge.append(b[ri])
            ri += 1

    while li < n:
        merge.append(a[li])
        li += 1

    while ri < m:
        merge.append(b[ri])
        ri += 1

    return merge

a = [2, 11, 7, 26, 32]
b = [5, 7, 12, 22, 27, 30]

s = Merge(a, b)
print(s)

#Container With Most Water
def MostWater(arr):
    l=0
    r=len(arr)-1
    mc=0
    while l<r:
        cap=(r-l)*min(arr[l],arr[r])
        mc=max(mc,cap)
        if arr[l]<=arr[r]:
            l+=1
        else:
            r-=1
    return mc
arr=[1,8,6,2,5,4,8,3,7]
v=MostWater(arr)
print(v)
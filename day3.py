#Majority Element
def majority(lt):
    n=len(lt)
    for i in range(n):
        c=0
        for j in range(n):
            if lt[i]==lt[j]:
                c+=1
                if n>n//2:
                    return lt[i]
    return -1
lt=[7,5,6,7,12,7,3,7,75,7]
m=majority(lt)
print(m)


#2

def majority(a):
    n = len(a)
    dic = {}

    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

        if dic[i] > n // 2:
            return i

    return -1

a = [2,8,4,5,2,8,4,8,8,9,8,5,8,8,8]

s = majority(a)
print(a)
print(s)


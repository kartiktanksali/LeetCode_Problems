def CountSub(s):
    count=0
    lst = []
    for i in s:
        for j in s:
            if s.index(i)!=s.index(j):
                if i!=j:
                    count+=1
            lst.append(count)
    return lst

s=input()
res=CountSub(s)
print(res)
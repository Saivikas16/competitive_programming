lst=[105,5,0]
l=len(lst)
i=0
m=-1
while(i<l):
    j=i+1
    while(j<l):
        s=set(str(lst[i]))
        t=set(str(lst[j]))
        if not len(s.intersection(t)):
            tmp=lst[i]+lst[j]
            m=max(m,tmp)
        j+=1
    i+=1
print(m)

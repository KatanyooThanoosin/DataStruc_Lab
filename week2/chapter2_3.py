def newRange(a): 
    k=[]
    if len(a)==1:
        s=0.0
        while s<a[0]:
            k.append(s)
            s+=1
    elif len(a)==2:
        s=a[0]
        while s<a[1]:
            k.append(s)
            s+=1
    else:
        s=a[0]
        while s<a[1]:
            k.append(s)
            s+=a[2]
    return k
print("*** New Range ***")
a=[float(i) for i in input("Enter Input : ").split()]
l=newRange(a)
for i in range(len(l)):
    l[i]=float("{:.3f}".format(l[i]))
print(tuple(l))

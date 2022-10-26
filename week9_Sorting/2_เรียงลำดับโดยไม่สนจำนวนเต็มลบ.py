l = [int(i)for i in input("Enter Input : ").split()]
lob = []
buak =[]
for i in range(len(l)):
    if l[i]<0:
        lob.append([l[i],i])
    else:
        buak.append(l[i])
l = buak
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
for i in lob:
    l.insert(i[1],i[0])
for i in l:print(i,end=" ")
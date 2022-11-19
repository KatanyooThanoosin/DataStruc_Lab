def combi(l,k,t=[],i=0):
    if i==len(l):
        if sum(t)==k:return [sorted(t)]
        return []
    
    s=[]
    a=combi(l,k,t,i+1)
    if a!=[]:s=a
    a=combi(l,k,t+[l[i]],i+1)
    if a!=[] and a!=s:s+=a
    return s
        
def moreThan(a,b):
    if len(a)>len(b):return True
    elif len(a)<len(b):return False
    else:
        for i in range(len(a)):
            if a[i]>b[i]:return True
            elif a[i]<b[i]:return False
        return False

k,inp = input("Enter Input : ").split("/")
l = combi([int(i)for i in inp.split()],int(k))
if l==[]:
    print("No Subset")
    exit()
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if moreThan(l[j],l[j+1]):
            l[j],l[j+1] = l[j+1],l[j]
for i in l:print(i)
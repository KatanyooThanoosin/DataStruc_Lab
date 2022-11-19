def combi(l,k,t=[],i=0):
    if i==len(l):return [t]if sum(t)==k else []
    return combi(l,k,t,i+1)+combi(l,k,t+[l[i]],i+1)
def moreThan(a,b):
    if len(a)!=len(b):return len(a)>len(b)
    for i in range(len(a)):
        if a[i]!=b[i]:return a[i]>b[i]
k,inp = input("Enter Input : ").split("/")
l = [[a.pop(a.index(min(a))) for q in a.copy()] for a in [list(k) for k in set(tuple(j) for j in combi([int(i)for i in inp.split()],int(k)))]]
if l==[]:print("No Subset")
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if moreThan(l[j],l[j+1]):l[j],l[j+1] = l[j+1],l[j]
for i in l:print(i)

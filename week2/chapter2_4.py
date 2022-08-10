a=[int(i) for i in input("Enter Your List : ").split()]
if len(a)<3:
    print("Array Input Length Must More Than 2")
    exit()
l=[]
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k]==0:
                if [a[i],a[j],a[k]] not in l:
                    l.append([a[i],a[j],a[k]])
print(l)
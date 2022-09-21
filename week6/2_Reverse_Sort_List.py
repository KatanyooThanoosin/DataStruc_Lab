def recursive(l,i=0):
    global s
    if len(l)==0:
        return 1
    elif len(s)==0 or i==len(s): 
        s.append(l[0])
        return recursive(l[1:])
    elif l[0]<s[i]:
        return recursive(l,i+1)
    else:
        s.insert(i,l[0])
        return recursive(l[1:])

l = [int(i) for i in input("Enter your List : ").split(",")]
s=[]
recursive(l)
print("List after Sorted :",s)

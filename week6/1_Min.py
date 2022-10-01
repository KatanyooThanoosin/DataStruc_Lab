def min(a):
    if len(a)==1:
        return a[0]
    elif a[0] > a[1]:
        return min(a[1:])
    else:
        a.pop(1)
        return min(a)
S = list(map(int , input("Enter Input : ").split()))
print("Min : "+str(min(S)))

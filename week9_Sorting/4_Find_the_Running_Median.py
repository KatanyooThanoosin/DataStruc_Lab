def insertion(l,sl=[],i=0,a=[]):
    if len(sl)==0:
        sl=[l.pop(0)]
        a=[sl[0]]
        print("list =",a,": median =",float(a[0]))
        return insertion(l,sl,0,a)
    elif i==len(sl) or l[0]<=sl[i]:
        sl.insert(i,l.pop(0))
        a.append(sl[i])
        print("list =",a,": median = ",end="")
        if len(sl)%2==0:
            print((sl[int(len(sl)/2)]+sl[int(len(sl)/2)-1])/2)
        else:
            print(float(sl[int(len(sl)/2)]))
        if len(l)==0:
            return sl
        return insertion(l,sl,0,a)
    else:
        return insertion(l,sl,i+1,a)

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    insertion(l)
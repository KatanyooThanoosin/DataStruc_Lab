l = [int(i)for i in input("Enter Input : ").split()]
countSwap = 0
for i in range(len(l)-1):
    isSwap = False
    lastSwap = None
    for j in  range(len(l)-1):
        if l[j]>l[j+1]:
            isSwap = True
            lastSwap = l[j]
            l[j],l[j+1] = l[j+1],l[j]
    if isSwap:
        countSwap += 1
        if(countSwap!=len(l)-1):
            print(countSwap,"step :",l,"move["+str(lastSwap)+"]")
print("last step :",l,"move["+str(lastSwap)+"]")

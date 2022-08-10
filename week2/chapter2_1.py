def Rshift(num,shift):
    a=bin(num)[2:]
    if num>0:
        if shift<len(a):
            return int(a[:-1*shift],2)
        else:
            return 0
    else:
        a=[i for i in a[1:]]
        if shift>=len(a):
            return -1
        else:
            for i in range(len(a)):
                a[i] = '1' if a[i]=='0' else '0'
            check = 1
            a=[int(i)for i in a]
            for i in range(len(a)-1,-1,-1):
                a[i]+=check
                if a[i]==2:
                    check = 1
                    a[i]=0
                else:
                    check=0
            s="".join([str(i)for i in a])[:-1*shift]
            a=[int(i) for i in s]
            check = 1
            for i in range(len(a)-1,-1,-1):
                a[i]-=check
                if a[i]==-1:
                    check = 1
                    a[i]=1
                else:
                    check=0
            for i in range(len(a)):
                a[i] = 1 if a[i]==0 else 0
            return -1*int("".join([str(i)for i in a]),2)
                
n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))
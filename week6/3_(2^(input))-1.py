def permu(s):
    if s==[]:
        print("0")
        return 1
    elif 2 in s:
        i = s.index(2)
        if i==0:
            return 1
        s[i-1]+=1
        s[i]=0
        return permu(s)
    else:
        print("".join([str(i)for i in s]))
        s[-1]+=1
        return permu(s)

n=int(input("Enter Number : "))
if n<0:
    print("Only Positive & Zero Number ! ! !")
    exit()
permu([0]*n)

def perket(a):
    if len(a)==1:
        return [abs(int(a[0].split()[0])-int(a[0].split()[1]))]
    else:
        return perket(a[:-1])

a=input("Enter Input : ").split(",")
print(sorted(perket(a))[0])
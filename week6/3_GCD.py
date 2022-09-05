def gcd(a,b):
    if a>b:return gcd(b,a)
    elif a==0:return b
    elif b==0:return a
    elif a<0:return gcd(-1*a,b)
    elif b<0:return gcd(a,-1*b)
    elif b%a==0:return a
    else:return gcd(abs(b%a),a)

a,b = [int(i)for i in input("Enter Input : ").split()]
if a==0 and b==0:
    print("Error! must be not all zero.")
elif (a==0 and b<0) or (b==0 and a<0):
    print("The gcd of",a,"and",b,"is :",abs(gcd(a,b)))
elif abs(a)>abs(b):
    print("The gcd of",a,"and",b,"is :",gcd(a,b))
else:
    print("The gcd of",b,"and",a,"is :",gcd(a,b))
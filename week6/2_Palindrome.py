def reverse(a):
    if len(a)>1:
        return a[-1]+reverse(a[0:len(a)-1])
    else:
        return a

a=input("Enter Input : ")
s="'"+a+"' is"
if a!=reverse(a):
    s+=" not" 
print(s,"palindrome")
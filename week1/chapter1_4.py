print("*** Fun with Drawing ***")
n=int(input("Enter input : "))
for i in range(n):
    s=""
    for j in range(n-i-1):
        s+="."
    s+="*"
    for j in range(2*i-1):
        s+="+"
    if i!=0:
        s+="*"
    for j in range(2*(n-i)-3):
        s+="."
    if i!=n-1:
        s+="*"
    for j in range(2*i-1):
        s+="+"
    if i!=0:
        s+="*"
    for j in range(n-i-1):
        s+="."
    print(s)
for i in range(2*n-2):
    s=""
    for j in range(i+1):
        s+="."
    s+="*"
    for j in range(2*n-3-i):
        s+="+"
    for j in range(2*n-4-i):
        s+="+"
    if i!=2*n-3:
        s+="*"
    for j in range(i+1):
        s+="."
    print(s)
def bon(w):
    a=[i for i in w]
    c=""
    for i in a:
        a.remove(i)
        if i in a:
            c = i
    return (ord(c)-ord('a')+1)*4
secretCode = input("Enter secret code : ")
print(bon(secretCode))
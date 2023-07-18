mQ=yQ=[]
for i in [[[int(k)for k in j.split(":")]for j in i.split()] for i in input("Enter Input : ").split(",")]:mQ,yQ=mQ+[i[0]],yQ+[i[1]]
al=["Eat","Game","Learn","Movie","Res.","ClassR.","SuperM.","Home"]
print("My   Queue =",", ".join(":".join(str(j)for j in i)for i in mQ)+"\nYour Queue =",", ".join(":".join(str(j)for j in i)for i in yQ)+"\nMy   Activity:Location =",", ".join(":".join([al[i[0]],al[i[1]+4]]) for i in mQ)+"\nYour Activity:Location =",", ".join(":".join([al[i[0]],al[i[1]+4]]) for i in yQ))
s=0
for i in range(len(mQ)):
    a,b=mQ.pop(0),yQ.pop(0)
    s=s+4 if a[0]==b[0] and a[1]==b[1] else(s+1 if a[0]==b[0]else (s+2 if a[1]==b[1]else s-5))
print(("Yes! You're my love!"if s>=7 else("Umm.. It's complicated relationship!"if s>0 else"No! We're just friends.")),f": Score is {s}.")

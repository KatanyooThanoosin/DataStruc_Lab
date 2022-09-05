def asteroid_collision(asts,i):
    if i==len(asts):
        return asts
    elif i==0 :
        return asteroid_collision(asts,i+1)
    elif asts[i]<0 and asts[i-1]>0:
        if abs(asts[i])<asts[i-1]:
            asts.pop(i)
        elif abs(asts[i])>asts[i-1]:
            asts.pop(i-1)
        else:
            asts.pop(i)
            asts.pop(i-1)
        return asteroid_collision(asts,0)
    else:
        return asteroid_collision(asts,i+1)
        

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,0))
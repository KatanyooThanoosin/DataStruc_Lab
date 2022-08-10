h,w = input("Enter your High and Weight : ").split()
b=float(w)/(float(h)**2)
if b<18.5:
    print("Less Weight")
elif b<23:
    print("Normal Weight")
elif b<25:
    print("More than Normal Weight")
elif b<30:
    print("Getting Fat")
else:
    print("Fat")
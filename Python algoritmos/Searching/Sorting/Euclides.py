def euclides(x,y):
    while y:
        x,y=y,x%y
    return x
n1=int(input("n1:"))
n2=int(input("n2:"))
mdc=euclides(n1,n2)
print(mdc)
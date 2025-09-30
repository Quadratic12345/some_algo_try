def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def f(l):
    x=l[0]
    for i in l[1:]:
        x=gcd(i,x)
        if x==1:
            return 1
    return x
l=list(map(int,input().split()))
print(f(l))

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def f(l,n):
    x=l[0]
    for i in range(1,n):
        x=gcd(x,l[i])
        if x==1:
            return n
    return 0
l=list(map(int,input().split()))
n=len(l)
print(f(l,n))
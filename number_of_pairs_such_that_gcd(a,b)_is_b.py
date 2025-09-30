def f(n):
    k=n
    x=1
    c=0
    while(x<=n):
        y=n/k
        c+=k*(y-x+1)
        x=y+1
        k=n/x
    return int(c)
n=int(input())
print(f(n))
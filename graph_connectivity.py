def g_connectivity(g,n,v=None):
    if v is None:
        v=set()
    v.add(n)
    print(n, end=" ")
    for ne in g.get(n,[]):
        if ne not in v:
            g_connectivity(g,ne,v)
    return len(v)==len(g)
g={
        'A':['B'],
        'B':[],
        'C':[],
}
start='A'
if g_connectivity(g,start):
    print("The graph is connected")
else:
    print("The graph is not connected")



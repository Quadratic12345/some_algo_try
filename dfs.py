def dfs(g,n,v=None):
    if v is None:
        v=set()
    v.add(n)
    print(n, end=" ")
    for ne in g[n]:
        if ne not in v:
            dfs(g,ne,v)
g={
        'A':['B'],
        'B':['C'],
        'C':[],
}
v=set()
dfs(g,'A',v)


def bfs(g,n,v):
    v.append(n)
    q.append(n)
    while q:
        x=q.pop(0)
        print(x,end=" ")
    for ne in g[x]:
        if ne not in v:
            v.append(ne)
            q.append(ne)
            bfs(g,ne,v)
g={
        'A':['B'],
        'B':['C'],
        'C':[],
}
v=[]
q=[]
bfs(g,'A',v)
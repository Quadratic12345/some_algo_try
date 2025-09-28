def cycle(g):
    v=set()
    s=set()
    def dfs(n):
        if n in s:
            return True
        if n in v:
            return False
        v.add(n)
        s.add(n)
        for ne in g.get(n,[]):
            if dfs(ne):
                return True
        s.remove(n)
        return False
    for n in g:
        if n not in v:
            if dfs(n):
                return True
    return False

g={
        'A':['B'],
        'B':['C'],
        'C':[],
}

if cycle(g)==True:
    print('There is cycle')
else:
    print('There is no cycle')
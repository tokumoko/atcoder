class UnionFind():
    par = []
    siz = []

    def __init__(self, x):
        self.par = [-1 for n in range(x)]
        self.siz = [1 for n in range(x)]

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]

uf = UnionFind(N)
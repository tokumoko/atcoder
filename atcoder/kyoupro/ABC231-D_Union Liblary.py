from functools import reduce
import math

# 引数Nをmax_num桁の文字列にして返す
# 例:
#     N = 124,max_num:3→ [1,2,4]
#     N = 124,max_num:4→ [0,1,2,4]
#     N = 124,max_num:2→ [2,4]
# N<0,max_num<0の場合は-1を返す
def get_digits(N,max_num):
    if N<0: return -1
    if max_num<0: return -1
    
    num = N
    array=[]
    for _ in range(max_num):
       rest = num%10
       num = int(num/10)
       array.append(rest)
        
    return list(reversed(array))

# 配列arrayの要素番号i以降でcがあるか線形に探索する
# cがある場合の要素番号を返す
# 例:
# array = [1,5,7,1,3],c = 1,index = 0 → 0
# array = [1,5,7,1,3],c = 1,index = 1 → 3
# array = [1,5,7,1,3],c = 3,index = 5 → 5
# array = [1,5,7,1,3],c = 9,index = 1 → -1
# array = [1,5,7,1,3],c = 3,index = -1 → -1
def search_right(array,c,index):
    if index < 0: return -1
    
    for i in range(index,len(array)):
        if array[i] == c: return i
    return -1

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group = n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
        self.group -= 1
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return self.group
 
    def all_group_members(self):
        dic = {r:[] for r in self.roots()}
        for i in range(self.n):
            dic[self.find(i)].append(i)
        return dic
 
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
 
# class UnionFind():
#     def __init__(self,n):
#         self.n = n
#         self.parents = [-1]*n
        
#     def find(self,x):
#         if self.parents[x] <0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def unite(self, x ,y):
#         rx = self.find(x)
#         ry = self.find(y)
#         if rx == ry:
#             return rx
#         else:
#             self.parents[ry] = rx
#             return rx

#     def same(self,x,y):
#         # print('==== same ====')
#         # print('parent[',x,']:',self.find(x))
#         # print('parent[',y,']:',self.find(y))
#         # print('========')
#         return self.find(x) == self.find(y)
        
        
        
def main():
    # 文字列の2進数を数値にする
    # '101' → '5'
    # 文字列の頭に'0b'をつけてint()にわたす
    # binary = int('0b'+'101',0)

    # 2進数で立っているbitを数える
    # 101(0x5) → 2
    # cnt_bit = bin(5).count('1')
    
    # N! を求める
    # f = math.factorial(N)

    # N の逆元
    # N_inv = pow(N,MOD-2,MOD)

    # nCr
    # Nの階乗 * rの階乗の逆元 * n-rの階乗の逆元
    
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    INF = float("inf")

    # 大きな素数
    MOD = 10**9+7
    
    # 1文字のみを読み込み
    # 入力:2
    # a = input().rstrip()
    # 変数:a='2'
    
    # スペース区切りで標準入力を配列として読み込み
    # 入力:2 4 5 7
    # a, b, c, d = (int(_) for _ in input().split())  
    # 変数:a=2 b=4 c=5 d =7
    
    # 1文字ずつ標準入力を配列として読み込み
    # 入力:2 4 5 7
    # a = list(int(_) for _ in input().split())
    # 変数:a = [2, 4, 5, 7]    

    # 1文字ずつ標準入力を配列として読み込み
    # 入力:2457
    # a = list(int(_) for _ in input())
    # 変数:a = [2, 4, 5, 7]    
    N, M = (int(_) for _ in input().split())
    UF = UnionFind(N)
    cnt = [0]*N
    for i in range(M):
        a_tmp, b_tmp = (int(_) for _ in input().split())
        a,b = a_tmp-1,b_tmp-1
        if UF.same(a,b):
            print("No")
            return
        UF.union(a,b)
        cnt[a] +=1
        cnt[b] +=1
            
    if max(cnt) >= 3:
        print("No")
    else:
        print("Yes")
        
if __name__ == '__main__':
    main()



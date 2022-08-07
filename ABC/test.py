r = [[] for _ in range(6)]
r[0] = [-1, 2, 4, 1, 3, -1]
r[1] = [3, -1, 0, 5, -1, 2]
r[2] = [1, 5, -1, -1, 0, 4]
for i in range(3):
  r[i+3] = 
print(r)
dice = list(map(int, input().split()))
q = int(input())
for i in range(q):
  a, b = map(int, input().split())
  a_ind = dice.index(a)
  b_ind = dice.index(b)
  print(dice[r[a_ind][b_ind]])

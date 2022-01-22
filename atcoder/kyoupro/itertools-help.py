import itertools
p=[1,2,3]
#pから2個並べる
print(list(itertools.permutations(p,2)))
#pから2個並べる(重複あり)
print(list(itertools.product(p,repeat=2)))
#pから2個選ぶ
print(list(itertools.combinations(p,2)))
#pから2個選ぶ(重複あり）
print(list(itertools.combinations_with_replacement(p,2)))

#ある値が何個あるか
gr = itertools.groupby([0,0,0,1,1,0,0,1,1,1,0])
for key, group in gr:
    print(f'{key}: {list(group)}')

#累積和
array=[1,2,3,4,5,6,7,8,9,10]
print(list(itertools.accumulate(array)))
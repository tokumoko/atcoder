n, q = map(int, input().split())
a = list(map(int, input().split()))
base = 1 << 17
seg_max = [0] * (2 * base)
def get_max(l, r, btm = 0, top = base, pos = 1):
    if l <= btm and top <= r:
        return seg_max[pos]
    if top <= l or r <= btm:
        return 0
    mid = (btm + top) // 2
    return max(get_max(l, r, btm, mid, pos * 2), get_max(l, r, mid, top, pos * 2 +1))
def set_val(l, r, val, btm=0, top=base, pos=1):
    
    return max(get_max(l, r, btm, mid, pos * 2), get_max(l, r, mid, top, pos * 2 + 1))
for i in range(n):
    a[i]
for i in range(n):
    l, r = map(int, input().split())
    
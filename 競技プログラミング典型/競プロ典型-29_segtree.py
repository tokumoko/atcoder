w, n = map(int, input().split())
base = 1 << 19
seg_max = [0] * (2 * base)
seg_change = [-1] * (2 * base)
def get_max(l, r, btm = 0, top = base, pos = 1):
    if l <= btm and top <= r:
        return seg_max[pos]
    if top <= l or r <= btm:
        return 0
    if seg_change[pos] != -1:
        seg_change[pos * 2] = seg_change[pos]
        seg_change[pos * 2 + 1] = seg_change[pos]
        seg_change[pos] = -1
        update(pos*2)
        update(pos*2+1)
    mid = (btm + top) // 2
    return max(get_max(l, r, btm, mid, pos * 2), get_max(l, r, mid, top, pos * 2 +1))
def update(x):
    seg_max[x] = max(seg_max[x],seg_change[x])
def set_val(l, r, val, btm=0, top=base, pos=1):
    if l <= btm and top <= r:
        seg_change[pos] = val
        update(pos)
        return
    if top <= l or r <= btm:
        return
    if seg_change[pos] != -1:
        seg_change[pos * 2] = seg_change[pos]
        seg_change[pos * 2 + 1] = seg_change[pos]
        seg_change[pos] = -1
        update(pos*2)
        update(pos*2+1)
    mid = (btm + top) // 2
    set_val(l, r, val, btm, mid, pos * 2)
    set_val(l, r, val, mid, top, pos * 2 + 1)
    seg_max[pos] = max(seg_max[pos],
                       seg_max[pos*2],
                       seg_max[pos*2+1])
    return max(get_max(l, r, btm, mid, pos * 2), get_max(l, r, mid, top, pos * 2 + 1))
    
for i in range(n):
    l, r = map(int, input().split())
    mx = get_max(l, r+1)
    print(mx + 1)
    set_val(l,r+1,mx+1)
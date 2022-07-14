s = list(input())
t = list(input())
pos = s[0]
cnt = 0
s_list = []
for i in range(len(s)):
    if s[i] == pos:
        cnt += 1
    else:
        s_list.append((pos, cnt))
        pos = s[i]
        cnt = 1
    if i == len(s) - 1:
        s_list.append((pos, cnt))
pos = t[0]
cnt = 0
t_list = []
for i in range(len(t)):
    if t[i] == pos:
        cnt += 1
    else:
        t_list.append((pos, cnt))
        pos = t[i]
        cnt = 1
    if i == len(t) - 1:
        t_list.append((pos, cnt))
if len(s_list) != len(t_list):
    print('No')
    exit()
flag = True
for i in range(len(s_list)):
    if s_list[i][0] == t_list[i][0]:
        if s_list[i][1] == t_list[i][1] or \
            (s_list[i][1] > 1 and \
                s_list[i][1] < t_list[i][1]):
            continue
    flag = False
print('Yes' if flag else 'No')
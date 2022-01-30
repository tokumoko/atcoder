from collections import deque
d = deque(list(input()))

print(d.pop())
# d
print(d)
# deque(['a', 'b', 'c', 'b'])
print(d.popleft())
# a
print(d)
# deque(['b', 'c', 'b'])
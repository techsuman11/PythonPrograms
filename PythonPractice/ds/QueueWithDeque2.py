from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(10)
q.appendleft(12)

print(q)
q.pop()
print(q)
q.popleft()
print(q)
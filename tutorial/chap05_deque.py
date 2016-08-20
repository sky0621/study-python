from collections import deque

queue = deque(["Taro", "Hanako", "Jiro"])
queue.append("John")
queue.append("Mary")

print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

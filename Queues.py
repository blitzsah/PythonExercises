# A queue is FIFO - First In First Out
# It is efficient to use DQ objects when working with FIFO so that memory isn't moved as much.

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # Removes the first item in the list (FIFO)
queue.popleft()
print(queue)


if not queue:
    print("empty")



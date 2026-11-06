class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        previous = node.prev
        nxt = node.next
        previous.next = nxt
        nxt.prev = previous

    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        node.prev = temp
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1
        self.remove(self.storage[key])
        self.insert(self.storage[key])
        return self.storage[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            node = self.storage[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return 
        node = Node(key, value)
        self.storage[key] = node
        self.insert(node)
        if len(self.storage) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.storage[node.key]

        

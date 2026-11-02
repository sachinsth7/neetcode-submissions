"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        lookup = {}
        while current:
            lookup[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            node = lookup[current]
            node.next = lookup[current.next] if current.next else None
            node.random = lookup[current.random] if current.random else None
            current = current.next
        return lookup[head] if head else None
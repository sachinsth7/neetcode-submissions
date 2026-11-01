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
        pointer = head
        lookup = {}
        while pointer:
            lookup[pointer] = Node(pointer.val)
            pointer = pointer.next
        pointer = head
        while pointer:
            node = lookup[pointer]
            node.next = lookup[pointer.next] if pointer.next else None
            node.random = lookup[pointer.random] if pointer.random else None
            pointer = pointer.next
        return lookup.get(head)
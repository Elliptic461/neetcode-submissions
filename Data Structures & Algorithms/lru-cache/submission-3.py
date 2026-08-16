# Creating a node for double linked list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap= capacity
        # Map key to node (value)
        self.cache = {}

        # left = LRU, right = most recent used
        self.left, self.right = Node(0,0), Node(0,0)
        
        # Initially pointing at each other
        self.left.next = self.right
        self.left.prev = None
        self.right.next = None
        self.right.prev = self.left
    
    # Remove node from list, helper function
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt 
        nxt.prev = prev
    
    # Insert node into list, helper function
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next =  nxt.prev = node
        node.prev = prev
        node.next = nxt



    def get(self, key: int) -> int:
        if key in self.cache:
            # Recently used, so reinsert it to the right most position
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If cap is exceed, remove LRU node
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        

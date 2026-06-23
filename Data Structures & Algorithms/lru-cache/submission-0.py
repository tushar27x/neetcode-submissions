class Node:
    def __init__(self, key: int, val:int):
        self.key, self.val = key, val
        self.next = self.prev = None
        
class LRUCache: 

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def _insert_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node: Node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self._insert_front(node)
        if len(self.cache) > self.capacity :
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCache:

    def __init__(self, capacity: int):
        self.start = Node()
        self.end = Node()
        self.start.nextt = self.end
        self.end.prev = self.start
        self.dict1 = {}
        self.cap = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict1:
            node = self.dict1[key]
            self.remove(node)
            self.insert(node)
            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict1:
            node = self.dict1[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            # dict1[key] = node

        else:
            node = Node()
            node.val = value
            node.key = key
            self.insert(node)
            self.cap += 1
            self.dict1[key] = node

            if self.cap>self.capacity:
                node = self.end.prev
                self.remove(node)
                del self.dict1[node.key]
                self.cap-=1


    def remove(self, node):
        prev = node.prev
        nextt = node.nextt
        prev.nextt = nextt
        nextt.prev = prev

    def insert(self, node):
        node.prev = self.start
        node.nextt = self.start.nextt
        node.nextt.prev = node
        self.start.nextt = node
        
            
class Node:
    def __init__(self, key = -1, val = -1, nextt = None , prev = None):
        self.key = key
        self.val = val
        self.nextt = nextt
        self.prev = prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
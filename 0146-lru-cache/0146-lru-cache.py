class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.mapper = defaultdict(ListNode)

    def get(self, key: int) -> int:
        if key not in self.mapper:
            return -1

        node = self.mapper[key]
        return_val = node.val
        self.remove(node)
        self.insert(node)
        return return_val

    def put(self, key: int, value: int) -> None:
        # if self.count>=capacity:
        if key not in self.mapper:
            node = ListNode(key= key, val = value)
            self.mapper[key] = node
            self.insert(node)
            self.count +=1

        else:
            node = self.mapper[key]
            self.remove(node)

            node.val = value
            self.insert(node)

        if self.count>self.capacity:
            lru_node = self.right.prev
            self.remove(lru_node)
            self.mapper.pop(lru_node.key)
            self.count-=1

    def remove(self, node):
        prev = node.prev
        next_n = node.next
        prev.next = next_n
        next_n.prev = prev

    def insert(self, node):
        temp = self.left.next
        self.left.next = node
        node.next = temp
        node.prev = self.left
        temp.prev = node
        # node.prev = 

class ListNode:
    def __init__(self,key = -1, val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
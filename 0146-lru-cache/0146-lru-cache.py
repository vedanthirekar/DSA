class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.capacity = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keymap = {}

    def get(self, key: int) -> int:
        if key in self.keymap:
            node = self.keymap[key]
            val = node.val
            self.remove(node)
            self.insert(node)
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keymap:
            node = self.keymap[key]
            node.key = key
            node.val = value
            self.remove(node)
            self.insert(node)

        else:
            node = ListNode(val = value, key = key)
            self.keymap[key] = node
            self.insert(node)
            self.capacity +=1

            if self.capacity>self.max_capacity:
                node = self.tail.prev
                key = node.key
                self.remove(node)
                self.capacity -=1
                del self.keymap[key]

    def insert(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev



            

class ListNode():
    def __init__(self, key= 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
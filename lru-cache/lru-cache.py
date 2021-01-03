class LRUCache:
​
    def __init__(self, capacity: int):
        self.queue = []
        self.cache = {}
        self.capacity = capacity
​
    def get(self, key: int) -> int:
        if key in self.queue:
            self.queue.pop(self.queue.index(key))
        self.queue.append(key)
        
        if key in self.cache:
            return self.cache[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        
        if key in self.queue:
            self.queue.pop(self.queue.index(key))
        self.queue.append(key)
        
        if len(self.cache) > self.capacity:
            key_to_remove = self.queue.pop(0)
            while key_to_remove not in self.cache:
                key_to_remove = self.queue.pop(0)
                
            self.cache.pop(key_to_remove)
​
​
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

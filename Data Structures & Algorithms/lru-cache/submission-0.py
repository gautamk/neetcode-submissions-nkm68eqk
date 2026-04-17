

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            # last=False => move to the beginning
            self.cache.move_to_end(key, last=False)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
        elif len(self.cache) == self.capacity:
            # remove the last item
            self.cache.popitem(last=True)
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
            
        
    
            

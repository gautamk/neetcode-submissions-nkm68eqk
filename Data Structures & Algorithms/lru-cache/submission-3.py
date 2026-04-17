

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            # move to the end to represent most recently used
            self.cache.move_to_end(key, last=True)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # remove the first item (Least Recently Used)
            self.cache.popitem(last=False)
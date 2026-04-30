class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value > -1:
            self.cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        # TODO check capacity, if exceeding, remove the oldest value
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

        

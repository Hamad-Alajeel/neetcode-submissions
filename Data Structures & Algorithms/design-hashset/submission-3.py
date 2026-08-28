class MyHashSet:

    def __init__(self):
        self.Set = set()

    def add(self, key: int) -> None:
        return self.Set.add(key)

    def remove(self, key: int) -> None:
        return self.Set.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.Set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
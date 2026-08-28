class MyHashMap:

    def __init__(self):
        self.map = [None]*10000

    def put(self, key: int, value: int) -> None:
        idx = key%10000
        self.map[idx] = (key,value)
        return None


    def get(self, key: int) -> int:
        idx = key%10000
        tuple = self.map[idx]
        if tuple is not None:
            return tuple[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        idx = key%10000
        self.map[idx] = None
        return None
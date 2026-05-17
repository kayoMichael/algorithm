from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.link_list = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.link_list:
            self.link_list.move_to_end(key)
            return self.link_list[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.link_list:
            self.link_list[key] = value
            self.link_list.move_to_end(key)
            return

        if len(self.link_list) == self.capacity:
            self.link_list.popitem(last=False)


        self.link_list[key] = value

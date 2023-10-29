import tinydb
from functools import lru_cache
class MyClass(object):
    db = tinydb.TinyDB("database.json")

    @lru_cache(maxsize=100, typed=True)
    def get_items_by_name(self, name):
        return self.db.search(tinydb.Query().name == name)


my_class = MyClass()

items = my_class.get_items_by_name("John Doe")

items = my_class.get_items_by_name("John Doe")

print(items)

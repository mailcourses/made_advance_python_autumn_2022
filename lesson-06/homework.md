# Домашнее задание к лекции #5

## 1. LRU-кеш без OrderedDict (+тесты).
    Интерфейс:

    class LRUCache:

        def __init__(self, limit=42):
            pass

        def get(self, key):
            pass

        def set(self, key, value):
            pass


    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"


    Если удобнее, get/set можно сделать по аналогии с dict:
    cache["k1"] = "val1"
    print(cache["k3"])


    Реализация любым способом.

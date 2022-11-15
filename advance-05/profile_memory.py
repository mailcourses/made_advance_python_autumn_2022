import time
from memory_profiler import profile
import weakref


class Engine:
    def __init__(self, car):
        self.car = weakref.ref(car)


class Car:
    def __init__(self):
        self.engine = Engine(self)


class A:
    def __init__(self, x):
        self.x = x


class Slots:
    __slots__ = ("x",)

    def __init__(self, x):
        self.x = x


@profile
def run_slots(n):
    objs = [A(i) for i in range(n)]
    slot_objs = [Slots(i) for i in range(n)]

    del objs
    del slot_objs



@profile
def run(n):
    # for i in range(n):
    #     time.sleep(0.1 * i)

    lst = [A(i) for i in range(n)]
    cars = {i: Car() for i in range(n)}


if __name__ == "__main__":
    # run(10000)
    run_slots(100_000)

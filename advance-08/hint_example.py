from typing import Union, Any
from collections.abc import Callable


Number = Union[int, float, complex]


#process.pyi


def add(a: Number, b: Number) -> Number:
    return a + b


def add2(a: Number) -> Number:
    return add(a, 2.0)


class Person:
    age: int = 0

class NoPerson:
    age: int = 0

def calc_mean_persons(persons: list[Person | NoPerson]) -> Number:
    if not persons:
        return 0
    return sum([p.age for p in persons]) / len(persons)



class BaseExp:
    age: int = 0

class ExpA(BaseExp):
    pass

class ExpB(BaseExp):
    pass

def calc_mean_exps(exps: list[BaseExp]) -> Number:
    return sum([p.age for p in exps]) / len(exps)


########


def calc_mean(nums: list[Number]) -> Number:
    if not nums:
        return 0
    return sum(nums) / len(nums)


def calc_mean_str(nums: list[Number]) -> str:
    if not nums:
        return str(0)
    return str(sum(nums) / len(nums))


def no_wrap(a, b):
    return a + b



def to_str(a: Number) -> str:
    return str(a)


def apply(func: Callable[[Number], str], num: Number) -> str:
    return func(num)


if __name__ == "__main__":
    print(add(1, 2))
    print(add2(1))

    assert calc_mean([1, 2, 3]) == 2
    assert calc_mean_str([1, 2, 3]) == "2.0", calc_mean_str([1, 2, 3])

    assert no_wrap("1", "2") == "12"

    mean_age = calc_mean_persons([Person(), Person()])
    assert mean_age == 0

    mean_age = calc_mean_persons([Person(), NoPerson()])
    assert mean_age == 0

    mean_age = calc_mean_exps([ExpA(), ExpB()])
    assert mean_age == 0

    # assert apply(round, 10) == 10


import random

def square(x):
    return x * x

def get_docs():
    return ["doc1", "doc2"]

def foo():
    return True


def my_super_function():
    pass

def compare(x):
    return -x

def main():
    print(square(10))

    for doc in get_docs():
        print(doc)

    my_super_function()

    l = list(range(0, 10))
    random.shuffle(l)
    # Signature: sorted(iterable, /, *, key=None, reverse=False)
    print(sorted(l, key=lambda x: -x, reverse=True) == sorted(l))
    print(l)

if __name__ == "__main__":
    main()

print(__name__)

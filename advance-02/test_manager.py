import multiprocessing


class A:
    def __init__(self, a):
        self.a = a


def update_data(data):
    data["qwerty"] = 2 ** 100
    data["a"] = A(10)


if __name__ == "__main__":
    data = {}
    proc = multiprocessing.Process(target=update_data, args=(data,))
    proc.start()
    proc.join()

    print(f"empty {data=}")

    with multiprocessing.Manager() as manager:
        data = manager.dict()
        proc = multiprocessing.Process(target=update_data, args=(data,))
        proc.start()
        proc.join()

        print(f"manager {data=}", data)

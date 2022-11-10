#! /usr/bin/env python

import cutils

def main():
    l = [1,2,3,4,5]
    res = cutils.sum(l, len(l))
    print(f"{res=}")
    assert res == sum(l)

if __name__ == "__main__":
    main()

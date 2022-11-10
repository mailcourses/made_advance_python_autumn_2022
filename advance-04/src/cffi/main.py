#! /usr/bin/env python

import cffi

def ABI():
    ffi = cffi.FFI()
    libc = ffi.dlopen('./lib2.so')
    ffi.cdef('''
    struct Point
    {
        int x;
        int y;
    };

    int area(struct Point *p1, struct Point *p2);
    ''')

    p1 = ffi.new('struct Point *')
    p2 = ffi.new('struct Point *')

    p1.x, p1.y = (10, 10)
    p2.x, p2.y = (3, 2)

    area = libc.area(p1, p2)
    print(f"Area of point1({p1.x}, {p1.y}) and point2({p2.x}, {p2.y}) is {area}")

def API():
    ffi = cffi.FFI()
    ffi.cdef('''
    int sum(int *arr, int len);
    ''')
    ffi.set_source('_sample', r'''
    #include <stdlib.h>

    int sum(int *arr, int len)
    {
        int res = 0;
        for (int i = 0; i < len; ++i)
        {
            res += arr[i];
        }
        return res;
    }
    ''')
    arr = [1, 2, 3, 4]
    c_arr = ffi.new('int []', arr)
    ffi.compile()

    from _sample import lib
    print(f"Result of sum function is {lib.sum(c_arr, len(c_arr))}")

def main():
    ABI()
    API()

if __name__ == "__main__":
    main()

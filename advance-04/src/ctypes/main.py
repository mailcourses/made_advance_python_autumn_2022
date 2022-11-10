#! /usr/bin/env python

import ctypes

def libc():
    lib_utils = ctypes.CDLL('utils.so')
    lib_utils.strstr2.argstype = [ctypes.c_char_p, ctypes.c_char_p]
    lib_utils.strstr2.restype = ctypes.c_char_p
    res = lib_utils.strstr2(b"ababac", b"baba")
    print(res)


def libcpp():
    lib_utils = ctypes.CDLL('libutilscpp.so')
    lib_utils.int2str.argstype = [ctypes.c_int]
    lib_utils.int2str.restype = ctypes.c_void_p

    lib_utils.free_memory.argstype = [ctypes.c_void_p]
    lib_utils.free_memory.restype = None

    res_str_p = lib_utils.int2str(100500)
    print(type(res_str_p))
    print(ctypes.c_char_p(res_str_p).value)
    lib_utils.free_memory(ctypes.c_char_p(res_str_p))

    lib_utils.fibonacci.argstype = [ctypes.c_int]
    lib_utils.fibonacci.restype = ctypes.c_int
    n = 10
    print(f"Fibonacci {n}-th number is: {lib_utils.fibonacci(n)}")

def main():
    print("=== libc ===")
    libc()
    print("=== libcpp ===")
    libcpp()

if __name__ == "__main__":
    main()

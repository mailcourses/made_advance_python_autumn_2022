#! /usr/bin/env python

import time
import ctypes

import cffi

import cutils
from cython import cyutils

FIBONACCI_N = 35

def fibonacci(n: int) -> int:
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def fibonacci_ctypes(n: int) -> int:
    lib_utils = ctypes.CDLL('ctypes/libutilscpp.so')
    lib_utils.fibonacci.argstype = [ctypes.c_int]
    lib_utils.fibonacci.restype = ctypes.c_int
    return lib_utils.fibonacci(FIBONACCI_N)

def fibonacci_cffi(n: int) -> int:
    ffi = cffi.FFI()
    lib = ffi.dlopen('./cffi/libutils.so')
    ffi.cdef('''
    int fibonacci(int n);
    ''')
    return lib.fibonacci(n)

def fibonacci_capi(n: int) -> int:
    return cutils.fibonacci(n)

def fibonacci_cython(n: int) -> int:
    return cyutils.fibonacci(n)

def main():
    start_ts = time.time()
    py_res = fibonacci(FIBONACCI_N)
    end_ts = time.time()
    print(f"[python] Time of execution pycode of fibonacci is {end_ts - start_ts} seconds")

    start_ts = time.time()
    ctypes_res = fibonacci_ctypes(FIBONACCI_N)
    end_ts = time.time()
    print(f"[ctypes] Time of execution ctypes-code of fibonacci is {end_ts - start_ts} seconds")

    start_ts = time.time()
    cffi_res = fibonacci_cffi(FIBONACCI_N)
    end_ts = time.time()
    print(f"[cffi] Time of execution cffi-code of fibonacci is {end_ts - start_ts} seconds")

    start_ts = time.time()
    capi_res = fibonacci_capi(FIBONACCI_N)
    end_ts = time.time()
    print(f"[capi] Time of execution capi-code of fibonacci is {end_ts - start_ts} seconds")

    start_ts = time.time()
    cython_res = fibonacci_cython(FIBONACCI_N)
    end_ts = time.time()
    print(f"[cython] Time of execution cython-code of fibonacci is {end_ts - start_ts} seconds")
    assert py_res == ctypes_res == cffi_res == capi_res == cython_res

if __name__ == "__main__":
    main()


cdef float x = 3.1415
cpdef float CONST = 100500.0

cpdef fibonacci(int n):
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

cpdef int dummy(int x):
    cdef int y = 100
    cdef int i
    for i in range(1, x + 1):
        y += i
    return y

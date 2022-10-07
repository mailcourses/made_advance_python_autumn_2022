#! /usr/bin/env python3

import heapq

def heapsort(lst):
    heapq.heapify(lst)
    res = []
    while lst:
        top = heapq.heappop(lst)
        res.append(top)
    return res

def main():
    pass

if __name__ == "__main__":
    main()

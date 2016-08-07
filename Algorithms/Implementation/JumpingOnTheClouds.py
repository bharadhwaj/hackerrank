#!/bin/python
import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
count = 0
i = 0
while i < n-1:
    if c[min(i+2,n-1)] == 1:
        count += 1
        i += 1
    else:
        count += 1
        i += 2
print count
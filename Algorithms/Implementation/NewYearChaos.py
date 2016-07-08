#!/bin/python

import sys
import math


T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    ans = 0
    error = False
    for i in range(n-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print "Too chaotic"
            error = True
            break
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                ans += 1
    if not error:
        print ans


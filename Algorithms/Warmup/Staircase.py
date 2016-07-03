#!/bin/python

import sys

n = int(raw_input().strip())
ns = n - 2
for stairs in range(1, n):
    print ' ' * ns, '#' * stairs
    ns -= 1
print '#' * n


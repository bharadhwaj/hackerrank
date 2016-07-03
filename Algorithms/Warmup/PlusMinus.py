#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print("{0:.6f}".format(round(len([x for x in arr if x > 0])/n,6)))
print("{0:.6f}".format(round(len([x for x in arr if x < 0])/n,6)))
print("{0:.6f}".format(round(len([x for x in arr if x == 0])/n,6)))


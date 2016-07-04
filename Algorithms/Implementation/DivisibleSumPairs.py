#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
count = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i]+a[j])%k == 0:
            count += 1
print count

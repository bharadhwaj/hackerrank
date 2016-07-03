t = input()
for i in range(t):
    n, m, s = [int(i) for i in raw_input().strip().split()]
    if (m%n+s-1)%n == 0:
        print n
    else:
        print (m%n+s-1)%n

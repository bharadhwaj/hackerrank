for i in range(int(raw_input())):
    n, k = map(int, raw_input().split(' '))
    a = map(int, raw_input().split(' '))
    if sum(j <= 0 for j in a) >= k:
        print 'NO'
    else:
        print 'YES'

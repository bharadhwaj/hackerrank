t = int(raw_input())
for i in range(t):
    n = raw_input()
    count = 0
    for j in n:
        if not int(j) == 0:
            if int(n)%int(j) == 0:
                count = count + 1
    print count

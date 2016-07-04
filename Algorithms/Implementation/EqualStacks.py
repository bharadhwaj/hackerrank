A = map(int,raw_input().strip().split(' '))
C1 = map(int,raw_input().strip().split(' '))
C2 = map(int,raw_input().strip().split(' '))
C3 = map(int,raw_input().strip().split(' '))

H1 = sum(C1)
H2 = sum(C2)
H3 = sum(C3)

N1 = []
N2 = []
N3 = []
if A.count(0) == 1:
    print 0
else:
    if H1 == H2 and H2 == H3 and H1 == H3:
        print H1
    else:
        for x in C1:
            H1 -= x
            N1.append(H1)
        for y in C2:
            H2 -= y
            N2.append(H2)
        for z in C3:
            H3 -= z
            N3.append(H3)
        small = N3
        if (N1 < N2 and N1 < N3):
            small = N1
        elif(N2 < N3):
            small = N2
        for x in small:
            if N1.count(x)!= 0 and N2.count(x) != 0 and N3.count(x) != 0:
                print x
                break

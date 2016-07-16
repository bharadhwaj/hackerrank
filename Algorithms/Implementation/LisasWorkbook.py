import pprint
def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

if __name__ == "__main__":
    n, k = map(int,raw_input().split(' '))
    t = map(int,raw_input().split(' '))
    page = []
    for i in t:
        for x in list(chunks(range(1,i+1),k)):
            page.append(x)
    count = 0
    for pn, val in enumerate(page):
        if pn+1 in val:
            count += 1
    print count
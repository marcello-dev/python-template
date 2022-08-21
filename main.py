def find_minsum_in_range(a, x, y):
    x -= 1
    # print('a',a)
    sub_array = a[x:y]
    sub_array.sort()
    if sub_array[0] >= 0:
        return sub_array[0]
    return sum(x for x in sub_array if x < 0)
        
if __name__ == "__main__":
    # filename = 'test.txt'
    filename = 'input.txt'
    with open(filename) as f:
        t = int(f.readline())
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        m = int(f.readline())
        queries = [ tuple(map(int, line.split())) for line in f]
    # t = int(input())
    # n = int(input())
    # a = list(map(int, input().split()))
    # m = int(input())
    # queries = [ tuple(map(int,input().split())) for _ in range(m) ]
    for query in queries:
        q, x, y = query
        # Swap
        if q == 0:
            a[x-1] = y
        # Print min sum in range
        else:
            min_sum = find_minsum_in_range(a, x, y)
            print(min_sum)
        
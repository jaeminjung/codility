def solution(X, A):
    if X == 1:
        return 0
    d = {}
    count = 0
    for (i, n) in enumerate(A):
        # print(n, i)
        if n <= X:
            if d.get(n) == None:
                d[n] = i
                count += 1
                if count == X:
                    return i
            else:
                d[n] = i
    # print(d)
    # for i in range(1, X+1):
    #     if d.get(i) == None:
    #         return -1
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(3, [1, 3, 1, 3, 2, 1, 3]))
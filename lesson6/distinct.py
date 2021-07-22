def solution(A):
    # write your code in Python 3.6
    d = {}
    ans = 0
    for n in A:
        if d.get(n) == None:
            ans += 1
            d[n] = 1
    return ans


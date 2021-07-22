def solution(A):
    # write your code in Python 3.6
    ans = 0
    number_c = 0
    for c in A:
        if c == 0:
            number_c += 1
        if c == 1:
            ans += number_c
    if ans > 1000000000:
        return -1
    return ans
    
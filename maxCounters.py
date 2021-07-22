
def solution(N, A):
    # write your code in Python 3.6
    li_ = [0] * N
    max_num = 0
    for num in A:
        if num <= N:
            li_[num-1] += 1
            if li_[num-1] > max_num:
                max_num = li_[num-1]
        else:
            li_ = [max_num] * N
    return li_


print(solution(1, [1]))
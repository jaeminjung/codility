def solution(A):
    # write your code in Python 3.6
    d = {}
    max_num = 0
    for num in A:
        if num > max_num:
            max_num = num
        if d.get(num) == None:
            d[num] = 0
            
    for i in range(1, max_num+1):
        if d.get(i) == None:
            return i
    return max_num+1
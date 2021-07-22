def solution(A):
    # write your code in Python 3.6
    d = {}
    max_num = 0
    total = 0
    for num in A:
        if d.get(num) == None:
            d[num] = 1
        else:
            return 0
        if num > max_num:
            max_num = num
        total += num
    
    result = max_num * (max_num + 1) / 2 - total
    
    if result == 0:
        return 1
    else:
        return 0
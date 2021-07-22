
def solution(N):
    # write your code in Python 3.6
    max_num = 0
    count = 0
    numbers = []
    flag = False
    while N>0:
        numbers.append(N % 2)
        N = N // 2
    print(numbers)

    if numbers.pop() == 0:
        return 0
        
    while numbers:
        element = numbers.pop()
        if element == 0:
            count += 1
        else:
            if max_num < count:
                max_num = count
            count = 0    
    return max_num

# print(solution(9))
# print(solution(529))
# print(solution(20))
# print(solution(32))
# print(solution(15))
# print(solution(1162))
print(solution(1610612737))
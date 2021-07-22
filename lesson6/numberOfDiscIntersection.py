
def solution1(A):
    ans = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            mid1 = i
            rad1 = A[i]
            mid2 = j
            rad2 = A[j]

            if mid2 - mid1 <= rad1 + rad2:
                if mid2 - mid1 + rad1 >= rad2:
                    ans += 1
                elif mid2 - mid1 + rad2 >= rad1:
                    ans += 1


    if ans > 10000000:
        return -1
    return ans

def solution(A):
    ans = 0
    helper_list = []
    for i in range(len(A)):
        left = i - A[i]
        right = i + A[i]
        helper_list.append((left, -1))
        helper_list.append((right, 1))
    helper_list.sort(key=lambda a: a[0])
    # print(helper_list)

    overlap = 0
    for num in helper_list:
        if num[1] == -1:
            ans += overlap
            overlap += 1
        if num[1] == 1:
            overlap -= 1
    if ans > 10000000:
        return -1
    return ans

def solution2(A):
    # write your code in Python 3.6
    arr = []

    for i, v in enumerate(A):
        arr.append((i-v, -1))
        arr.append((i+v, 1))

    arr.sort()
    intersect = 0
    intervals = 0

    for i, v in enumerate(arr):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersect += intervals
            intervals += 1
    if intersect > 10000000:
        return -1
    return intersect
print(solution([1,5,2,1,4,0]))
print(solution([1, 1, 1]))
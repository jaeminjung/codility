
def solution(A):
    d = {}
    half = len(A) / 2
    for num in A:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    a = []
    for i, n in enumerate(d.items()):
        a.append(n)
    a.sort(key=lambda x:x[1])
    if a[-1][1] > half:
        return A.index(a[-1][0])
    
    return -1
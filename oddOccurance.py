
def solution(A):
    
    d = {}
    for num in A:
        if d.get(num) == None:
            d[num] = 0
        else:
            del d[num]
    one = d.popitem()
    return one[0]

print(solution( [9, 3, 9, 3, 9, 7, 9]))

d = {}
d['a'] = 3
d[5] = 0
print(d.get('b') == None)
print(d.get(5))

del d[5]
print(d.popitem())
print(d)
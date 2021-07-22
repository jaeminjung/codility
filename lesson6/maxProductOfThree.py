
def solution(A):
    max_product = A[0] * A[1] * A[2]

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            for k in range(j+1, len(A)):
                product = A[i] * A[j] * A[k]
                if product > max_product:
                    max_product = product
    return max_product

def solution(A):
    A = sorted(A, reverse=True)
    candidate1 = A[0] * A[1] * A[2]
    candidate2 = A[-1] * A[-2] * A[0]

    if candidate1 > candidate2:
        return candidate1
    else:
        return candidate2
    
print(solution([-3, 1,2,-2,5,6]))
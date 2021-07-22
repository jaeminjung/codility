def solution(A, B, K):
    
    count = 0
    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0
    while True:
        # if A > K:
        #     break
        if A % K == 0:
            count += 1
            break
        if A > B:
            break
        A += 1

    count += (B-A) // K
    
    return count

print(solution(0,1,1))
print(solution(1,1,11))

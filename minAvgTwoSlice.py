
def solution1(A):
    less = (A[0] + A[1]) / 2
    ans = 0
    count = 2
    while count <= len(A):
        
        for i in range(0, len(A) - count + 1):
            sum = 0
            for j in range(count):
                sum += A[i + j]
            avg = sum / count
            if avg < less:
                less = avg
                ans = i
        
        count += 1

    return ans

def solution(A):
    ans = 0
    min_avg = (A[0] + A[1]) / 2
    for i in range(len(A)):
        try:
            compare = (A[i] + A[i+1]) / 2
            if compare < min_avg:
                ans = i
                min_avg = compare
            
            compare = (A[i] + A[i+1] + A[i+2]) / 3
            if compare < min_avg:
                ans = i
                min_avg = compare
        except:
            break

    return ans


print(solution([4,2,2,5,1,5,8])) # 1
print(solution([-3, -5, -8, -4, -10])) # 2
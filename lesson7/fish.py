def solution(A, B):
    # write your code in Python 3.6
    queue = []
    queue.append(A[0])
    curr = B[0]
    for i in range(1, len(A)):
        if curr == 0:
            if B[i] == 0:
                queue.append(A[i])
            else:
                curr = 1
                queue.append(A[i])
        else: # curr = 1
            if B[i] == 0:
                if len(queue) == 0:
                    curr = 1
                    queue.append(A[i])
                else:
                    pop = queue.pop()
                    
                    if pop > A[i]:
                        queue.append(pop)
                        continue
                    else:
                        queue.append(A[i])
                        curr = 0
            else:
                queue.append(A[i])
    return len(queue)

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
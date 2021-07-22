
def solution1(S, P, Q):
    # write your code in Python 3.6
    d = {'A':1, 'C':2, 'G':3, 'T':4}
    ans = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        less = d[S[start]]
        for j in range(start+1, end+1):
            if less == 1:
                break
            compare = d[S[j]]
            if compare < less:
                less = compare
        ans.append(less)   
    return ans

def solution_helper(arr, start, end):
    idx = 0
    while idx < len(arr):
        if arr[idx] >= start:
            break
        idx += 1
    try:
        if arr[idx] <= end:
            return True
    except:
        return False

def solution2(S, P, Q):
    ans = []
    As = []
    Cs = []
    Gs = []
    Ts = []
    for (i, s) in enumerate(S):
        if s == 'A':
            As.append(i)
        elif s == 'C':
            Cs.append(i) 
        elif s == 'G':
            Gs.append(i)
        else:
            Ts.append(i)
    
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        if solution_helper(As, start,end):
            ans.append(1)
        elif solution_helper(Cs, start, end):
            ans.append(2)
        elif solution_helper(Gs, start, end):
            ans.append(3)
        else:
            ans.append(4)

    return ans


def solution(S, P, Q):
    ans = []

    for i in range(len(P)):
        start = P[i]
        end = Q[i]

        slice_s = S[start:end+1]
        if 'A' in slice_s:
            ans.append(1)
        elif 'C' in slice_s:
            ans.append(2)
        elif 'G' in slice_s:
            ans.append(3)
        else:
            ans.append(4)
    return ans


print(solution('CAGCCTA', [2,5,0], [4,5,6])) # [2,4,1]
print(solution('A', [0], [0])) # [1]
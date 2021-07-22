
def solution(S):
    q = []
    d = {'}':'{', ']':'[', ')':'('}
    
    for s in S:
        if d.get(s) is None:
            q.append(s)
        else:
            try:
                if q[-1] == d[s]:
                    q.pop()
                    continue
            except:
                pass
            q.append(s)
    
    return 1 if len(q) == 0 else 0

    pass

print(solution("(()(())())"))
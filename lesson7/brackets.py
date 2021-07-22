
def solution(S):
    d = {')':'(', '}':'{', ']':'['}
    queue = []

    for s in enumerate(S):
        # print(s)
        try:
            if d[s[1]] == queue[-1]:
                queue.pop()
                continue
        except:
            pass
        
        queue.append(s[1])
    # print(queue)
    if len(queue) == 0:
        return 1
    else:
        return 0

print(solution('([)()]'))
print(solution('{[()()]}'))
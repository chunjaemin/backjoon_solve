import math 
# 3700 3 
def solution(numbers):
    N = len(numbers)
    if sum(numbers) == 0:
        return "0"
    sn = [str(x) for x in numbers]
    sn.sort(key = lambda x : x * 3, reverse=True)
    # print(sn)
    ans =''
    for x in sn:
        ans += x

    return ans

numbers = [0, 0, 0]

print(solution(numbers))


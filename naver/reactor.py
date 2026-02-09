import sys
input =sys.stdin.readline 

nums = [3, 1, 2] # 1 3 0 | 2 1 1 | 0 2 1 | 1 0 2 | 1 1 0  
N = len(nums)

time = 0
check = 1 
while check == 1:
    time += 1
    check = 0 
    
    diff = [0] * (N)
    # print(nums)
    for i in range(N):
        if nums[i] > 1:
            check = 1 
            for di in (-1, 1):
                diff[i] -= 1
                if 0<= i + di< N:
                    diff[i + di] += 1 
    for i in range(N):
        nums[i] += diff[i]
    # print(nums)
    # print()

print(time- 1)
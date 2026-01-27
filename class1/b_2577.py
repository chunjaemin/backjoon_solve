import sys
input = sys.stdin.readline

num = 1 
for i in range(3):
    n = int(input().rstrip())
    num *= n 


n_str = str(num)

for i in range(10):
    print(n_str.count(str(i)))
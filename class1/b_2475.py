import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

ans = sum(x**2 for x in arr)

ans = ans %10

print(ans)
import sys
from collections import defaultdict
input = sys.stdin.readline 


# 일반, 특별, 서비스 메뉴
# 특별 => 일반 20000원 이상 주문시
# 서비스 => 일반메뉴 + 특별메뉴 50000원 이상 주문시

A, B, C = map(int, input().split())

food = defaultdict(list) #1 = 일반, 2 = 특수, 3 = 서비스 
for _ in range(A):
    name, price = input().split()
    price = int(price)
    food[name] = [1, price]
for _ in range(B):
    name, price = input().split()
    price = int(price)
    food[name] = [2, price]

for _ in range(C):
    name =input().rstrip()
    food[name] = [3, 0]

# print(food)

normal_p = 0
special_p = 0

special_cnt = 0 
service_cnt = 0 # 개수 
N = int(input())
for i in range(N):
    S = input().rstrip()
    t, price = food[S]
    if t == 1:
        normal_p += price 
    if t == 2:
        special_p += price 
        special_cnt += 1 
    if t== 3: 
        service_cnt += 1 
    
ans = "Okay"
if special_cnt > 0:
    if normal_p < 20000:
        ans = "No"

if service_cnt > 0:
    if service_cnt != 1:
        ans = "No"
    if normal_p + special_p < 50000:
        ans = "No"

print(ans)
    # print(S)


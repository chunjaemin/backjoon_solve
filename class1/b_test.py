import sys
input = sys.stdin.readline

N = int(input())

primes = list(map(int, input().split()))

cnt= 0
for x in primes:
    isprime = True
    if x != 1:
        for i in range(2, x):
            if x % i == 0:
                isprime = False
    else: 
        isprime = False
    if isprime:
        cnt +=1 
        
print(cnt)
'''
# 単一の整数
N = int(input().strip())
# 2つの整数
A, B = map(int, input().split())
# 1行に複数整数 -> リスト
arr = list(map(int, input().split()))
# N行にわたる整数 -> リスト
arr_N = [int(input()) for _ in range(N)]
# M行にわたるペア整数 -> リスト of tuple
pairs = [list(map(int, input().split())) for _ in range(N)]

if f:
    print("Yes")
else:
    print("No")
'''

import sys
sys.stdin = open('code/input/input.txt', encoding='utf-8-sig')


n, k, p, q, r = map(int, input().split())

s = 100**k
t = 10**9+7

A = []
for i in range(n):
    a = int(input())
    A.append(a)
    
#print(A)
A_mean = A
for i in range(k):
    cal = 0
    A1 = []
    for a in A_mean:
        cal += a
        A1.append(cal)
        
    cal = 0
    A2 = []
    for a in reversed(A_mean):
        cal += a
        A2.append(cal)
    
    A3 = A_mean
    for j in range(n):
        A_mean[j] = (A1[j] * p + A2[j] * q + A3[j] * r)/100
    print(A1)
    print(A2)
    print(A_mean)

ans = sum(A_mean)
print(int((ans*s)%t))
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

t = []
for _ in range(3):
    tmp = int(input())
    t.append(tmp)
    # print(tmp)

print(max(t))

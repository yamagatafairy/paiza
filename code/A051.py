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

h, w = map(int, input().split())
grid = []
for i in range(h):
    row = list(map(int, input().split()))
    grid.append(row)
    # print(tmp)

# dp = [[0 for _ in range(w)]]*h # value 
dp = grid[:]
# print(dp)
# print(grid)

for i, g in enumerate(grid):
    if i == h - 1:
        break
    for j in range(w):
        if j == 0:
            tmp = max(g[0], g[1])
        elif j == w-1:
            if w == 1:
                tmp = g[0]
            else:
                tmp = max(g[w-1],g[w-2])
        else:
            tmp = max(g[j-1], g[j], g[j+1])
        dp[i+1][j] += tmp

# print(dp)
print(max(dp[h-1]))
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

from collections import defaultdict, deque
h, w = map(int, input().split())
grid = []
for i in range(h):
    row = list(input().split())
    grid.append(row)

# print(grid)

dirs = defaultdict(set)
dirs_r = defaultdict(set)
all = set()
dq= deque()

n = int(input())
for i in range(n):
    a, b = input().split()
    # print(a, b)
    dirs[a].add(b)
    dirs_r[b].add(a)
    all.add(a)
    all.add(b)

cnt = 0
while dirs_r and cnt < 20:
    hosyoku_animal = all - set(dirs_r.keys())
    
    for a in hosyoku_animal:
        dq.append(a)
    
    tmp = set(dirs_r.keys())
    #print(dirs_r)
    for key, _ in list(dirs_r.items()):
        # print(key)
        dirs_r[key] -= hosyoku_animal
        if not dirs_r[key]:
            del dirs_r[key]
    all = tmp
    #print(dirs_r, cnt)
    cnt += 1
    #print(dq)

'''
print(dirs)
print(dirs_r)
print(all)
print(dq[0])
'''
move = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
while dq:
    # print('dq', dq)
    tmp = dq.popleft()
    del_ani = dirs[tmp]
    # print('del_ani', del_ani)
    for i in range(h):
        for j in range(w):
            if tmp == grid[i][j]:
                for ci, cj in move:
                    ci = i + ci
                    cj = j + cj
                    if (0 <= ci < h) and (0 <= cj < w):
                        if grid[ci][cj] in del_ani:
                            grid[ci][cj] = '-'



for g in grid:
    print(*g)
    
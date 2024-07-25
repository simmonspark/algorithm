import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int,input().strip().split())

A = [list(map(int,input().strip().split())) for _ in range(M)]
visit = [[False]*N for _ in range(M)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

que = deque()



for i in range(M):
    for j in range(N):
        if A[i][j] == 1:
            que.append((i, j))
            visit[i][j] = True
def BFS():
    while que:
        curr_x, curr_y = que.popleft()
        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]
            if 0 <= new_x < M and 0 <= new_y < N and A[new_x][new_y] == 0:
                if not visit[new_x][new_y]:
                    visit[new_x][new_y] = True
                    A[new_x][new_y] = A[curr_x][curr_y] + 1
                    que.append((new_x, new_y))
BFS()
day = 0
for i in range(M):
    for j in range(N):
        if A[i][j] == 0:
            print(-1)
            sys.exit()
        if A[i][j] > day:
            day = A[i][j]
print(day-1)


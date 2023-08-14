# 1238_파티_party
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

adjL = [[] for _ in range(N+1)]
adjL2 = [[] for _ in range(N+1)]
visited = [0]*(N+1)
visited2 = [0]*(N+1)
for _ in range(M):
    s, g, t = map(int, input().split())
    adjL[g].append([s, t])
    adjL2[s].append([g, t])

stack = [[X, 0]]
stack2 = [[X, 0]]
visited[X] = 1
visited2[X] = 1
ans = 0
while stack:
    node, dis = stack.pop()

    for v in adjL[node]:
        if visited[v[0]] == 0 or visited[v[0]] > dis+v[1]:
            stack.append([v[0], dis + v[1]])
            visited[v[0]] = dis + v[1]

while stack2:
    node, dis = stack2.pop()

    for v in adjL2[node]:
        if visited2[v[0]] == 0 or visited2[v[0]] > dis+v[1]:
            stack2.append([v[0], dis + v[1]])
            visited2[v[0]] = dis + v[1]

for i in range(1, N+1):
    if (visited[i] + visited2[i]) > ans:
        ans = (visited[i] + visited2[i])
print(ans)

import heapq


def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 갱신해줄필요없다 ( 거리가 더 짧다 ) 그럼 패스
            continue
        #거리가 크다면
        for now1, dist1 in graph[now]: # 연결된거 다 탐색하자,,
            if dist+dist1 < distance[now1]: # 갱신해주자
                distance[now1] = dist+dist1 # 갱신해주면 뭐해야되지,,
                heapq.heappush(q, (dist+dist1, now1))



n,m,x = map(int,input().split())
INF = float('inf')
graph = [[] for _ in range(n+1)]
visited = [False] *(n+1)
for _ in range(m):
    start, end, time = map(int,input().split())
    graph[start].append((end,time))
# print(graph)

answer = [[0]*(n+1)]
for i in range(1,n+1):
    distance = [INF]*(n+1)
    dijk(i)
    answer.append(distance)
# print(answer)
maxx = 0
for i in range(1,n+1):
    if i == x:
        continue
    if maxx < answer[i][x]+answer[x][i]:
        maxx =answer[i][x]+answer[x][i]
print(maxx)

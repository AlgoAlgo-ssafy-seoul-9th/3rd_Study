n,m = map(int,input().split())
dic = {}
for _ in range(n):
    eng = input()
    if len(eng) < m:
        continue
    if eng in dic:
        dic[eng] += 1
    else:
        dic[eng] = 1
sordic = (sorted(dic.items(),key=lambda x:(-x[1],-len(x[0]),x[0])))
for i in (list(sordic)):
    print(i[0])

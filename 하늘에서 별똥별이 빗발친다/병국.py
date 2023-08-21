N, M, L, K = map(int, input().split())

# N,M 은 사실상 의미가없네,, 별똥별의 위치에맞게 하면되니까 for문을 K로 해도됨
stars = []
for i in range(K):
  x, y = map(int, input().split())
  stars.append((x,y))
answer = 0
for i in range(K):
    for j in range(K):
        cnt = 0
        for k in range(K):
            if stars[i][0]<=stars[k][0]<=stars[i][0]+L and stars[j][1]<=stars[k][1]<=stars[j][1]+L:
                cnt += 1
        answer = max(answer,cnt)
        # 튕겨내는게 answer
real = K-answer
# 지구에 추락 ㅠㅠ 하는게 real
print(real)

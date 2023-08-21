n = int(input())
m = list(input())
# 레드, 블루 선택
# 왼쪽, 오른쪽으로 보낼지 선택
# 총 4가지 중 최소 구하기

#  레드 선택했을 때 먼저 오른쪽으로옮기자
cnt = 0
red = 0
blue = 0
answer = []
# 예시는 RRBRRB


# 오른쪽으로 옮기기 R, B 순으로
for i in range(n):
    if m[i] == 'R':   # R 나오면 red +1 해준다
        red += 1
    if m[i] == 'B' and red: # B가 나왔을 때, 근데 이미 레드가 나왔을때
        cnt += red # 이때까지 센 레드 다 더해줘,, 오른쪽으로 옮겨야하니까,,
        red = 0 # 레드 초기화,, 계속 진행. 그럼 4가 나오겠군0,,
answer.append(cnt)
cnt = 0
for i in range(n):
    if m[i] == 'B':
        blue += 1
    if m[i] == 'R' and blue:
        cnt += blue
        blue = 0
answer.append(cnt)

# 이제 왼쪽으로 옮기는거

cnt = 0
for i in range(n-1,-1,-1):
    if m[i] == 'R':   # R 나오면 red +1 해준다
        red += 1
    if m[i] == 'B' and red: # B가 나왔을 때, 근데 이미 레드가 나왔을때
        cnt += red # 이때까지 센 레드 다 더해줘,, 오른쪽으로 옮겨야하니까,,
        red = 0 # 레드 초기화,, 계속 진행. 그럼 4가 나오겠군0,,
answer.append(cnt)
cnt = 0
for i in range(n-1,-1,-1):
    if m[i] == 'B':
        blue += 1
    if m[i] == 'R' and blue:
        cnt += blue
        blue = 0
answer.append(cnt)

print(min(answer))


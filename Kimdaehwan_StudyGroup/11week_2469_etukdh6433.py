import sys

N = int(sys.stdin.readline())
L = int(sys.stdin.readline())

bridge = [[] for i in range(L)]                 # 각 라인별 bridge를 저장하는 배열
al = [chr(i) for i in range(65, 65+N)]          # 시작할때의 알파벳 배열
ar_al = list(sys.stdin.readline().rstrip())     # 모든 bridge를 지난 후의 알파벳 배열 입력

an_b = []                                       # ?????에 입력되었어야할 bridge 결과가 없을 경우 xxxxxx로 출력
c = 0

for i in range(L):
    bridge[i] = list(sys.stdin.readline().rstrip())

for j in range(L):
    if bridge[j][0] == '?':                     # ????인 bridge의 라인 j값을 알아낸다.
        break
    else:                                       # bridge배열을 통해 al배열을 재배열한다.
        for k in range(N-1):
            if bridge[j][k] == '-':
                al[k], al[k+1] = al[k+1], al[k]

for l in range(L-1, j, -1):                     # 마지막 bridge 부터 ????이전 라인 까지 실행
    for m in range(N-1):
        if bridge[l][m] == '-':
            ar_al[m], ar_al[m+1] = ar_al[m+1], ar_al[m]

for n in range(N-1):
    if ar_al[n] == al[n]:                       # ar_al[n]값과 al[n]값이 같을 경우 bridge에 '*'을 추가
        an_b.append('*')
    else:
        an_b.append('-')                        # ar_al[n]값과 al[n]값이 다를 경우 bridge에 '-'을 추가
        al[n], al[n+1] = al[n+1], al[n]

for o in range(N-1):
    if an_b[o] == '-':                          # '-'일 경우 c값을 1증가
        c += 1
        if c > 1:
            break
    else:
        c = 0

if ar_al == al and c < 2:
    print(f"{''.join(p for p in an_b)}")
else:
    print(f"{'x'*(N-1)}")
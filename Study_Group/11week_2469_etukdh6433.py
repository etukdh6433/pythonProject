import sys

N = int(sys.stdin.readline())
L = int(sys.stdin.readline())

bridge = [[] for i in range(L)]
al = [chr(i) for i in range(65, 65+N)]
ar_al = list(sys.stdin.readline().rstrip())

an_b = []
c = 0

for i in range(L):
    bridge[i] = list(sys.stdin.readline().rstrip())

for j in range(L):
    if bridge[j][0] == '?':
        break
    else:
        for k in range(N-1):
            if bridge[j][k] == '-':
                al[k], al[k+1] = al[k+1], al[k]

for l in range(L-1, j, -1):
    for m in range(N-1):
        if bridge[l][m] == '-':
            ar_al[m], ar_al[m+1] = ar_al[m+1], ar_al[m]

for n in range(N-1):
    if ar_al[n] == al[n]:
        an_b.append('*')
    else:
        an_b.append('-')
        al[n], al[n+1] = al[n+1], al[n]

for o in range(N-1):
    if an_b[o] == '-':
        c += 1
        if c > 1:
            break
    else:
        c = 0

if ar_al == al and c < 2:
    print(f"{''.join(p for p in an_b)}")
else:
    print(f"{'x'*(N-1)}")
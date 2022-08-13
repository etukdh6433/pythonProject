"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
22주차 6603 로또
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from itertools import *
#
# while True:
#     lotto = list(map(int, sys.stdin.readline().split()))
#
#     if lotto[0] == 0:
#         break
#
#     co_list = list(combinations(lotto[1:], 6))
#
#     for i in co_list:
#         print(*i)
#     print()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
22주차 2468 안전 영역
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
# field = []
# result = []
#
# for _ in range(N):
#     field.append(list(map(int, sys.stdin.readline().split())))
#
#
# def area(a, b):
#     q = deque([(a, b)])
#     dr = [[1, 0], [-1, 0], [0, -1], [0, 1]]
#     cnt = 1
#
#     while q:
#         ux, uy = q.popleft()
#         for i in range(4):
#             x = ux + dr[i][0]
#             y = uy + dr[i][1]
#             if (0 <= x < N) and (0 <= y < N) and (water[y][x] == 0):
#                 water[y][x] = 1
#                 q.append((x, y))
#                 cnt += 1
#
#     return cnt
#
#
# for k in range(101):
#     length = []
#     water = [[0 for _ in range(N)] for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if field[i][j] <= k:
#                 water[i][j] = 1
#
#     for i in range(N):
#         for j in range(N):
#             if water[i][j] == 0:
#                 water[i][j] += 1
#                 length.append(area(j, i))
#
#     result.append(len(length))
#
# print(max(result))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
22주차 1697 숨바꼭질
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
#
# N, K = map(int, sys.stdin.readline().split())
# visit = [False for _ in range(100001)]
#
#
# def seek(a):
#     visit[a] = True
#     q = deque([a])
#     c = 0
#     while q:
#         for i in range(len(q)):
#             un = q.popleft()
#             if un == K:
#                 return c
#             if un - 1 >= 0 and not visit[un - 1]:
#                 visit[un - 1] = True
#                 q.append(un - 1)
#             if un + 1 < 100001 and not visit[un + 1]:
#                 visit[un + 1] = True
#                 q.append(un + 1)
#             if un * 2 < 100001 and not visit[un * 2]:
#                 visit[un * 2] = True
#                 q.append(un * 2)
#         c += 1
#
#
# print(seek(N))

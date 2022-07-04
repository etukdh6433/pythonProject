"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
17주차 2206 벽 부수고 이동하기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
#
#
# def find(arr):
#     dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     dist = [[[0, 0] for i in range(c)] for j in range(r)]
#     dist[0][0][0] = 1
#     q = deque([(0, 0, 0)])
#
#     while q:
#         pr, pc, w = q.popleft()
#
#         if (pr == r - 1) and (pc == c - 1):
#             return dist[-1][-1][w]
#
#         for k in range(4):
#             nr = pr + dir[k][0]
#             nc = pc + dir[k][1]
#
#             if (0 <= nr) and (nr < r) and (0 <= nc) and (nc < c) and (dist[nr][nc][w] == 0):
#
#                 if arr[nr][nc] == 0:
#                     q.append((nr, nc, w))
#                     dist[nr][nc][w] = dist[pr][pc][w] + 1
#
#                 if w == 0 and arr[nr][nc] == 1:
#                     q.append((nr, nc, 1))
#                     dist[nr][nc][1] = dist[pr][pc][w] + 1
#     return -1
#
#
# r, c = map(int, sys.stdin.readline().split())
# nl = []
# for i in range(r):
#     nl.append(list(map(int, sys.stdin.readline().rstrip())))
#
# print(find(nl))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
17주차 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
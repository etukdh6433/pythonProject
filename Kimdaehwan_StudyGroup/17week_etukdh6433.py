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
17주차 3055 탈출
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
#
#
# def find(arr):
#     dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     dist = [[False for i in range(c)] for j in range(r)]
#     sonic = deque()
#     water = deque()
#     count = 0
#
#     for i in range(r):
#         for j in range(c):
#             if arr[i][j] == '*':
#                 water.append((i, j))
#                 dist[i][j] = True
#             elif arr[i][j] == 'S':
#                 sonic.append((i, j))
#                 dist[i][j] = True
#             elif arr[i][j] == 'X':
#                 dist[i][j] = True
#
#     while sonic:
#         for i in range(len(water)):
#             wx, wy = water.popleft()
#             for j in range(4):
#                 nx = wx + dir[j][0]
#                 ny = wy + dir[j][1]
#                 if (0 <= nx) and (nx < r) and (0 <= ny) and (ny < c):
#                     if arr[nx][ny] == '.':
#                         water.append((nx, ny))
#                         arr[nx][ny] = '*'
#                         dist[nx][ny] = True
#
#         count += 1
#
#         for i in range(len(sonic)):
#             sx, sy = sonic.popleft()
#             for j in range(4):
#                 nx = sx + dir[j][0]
#                 ny = sy + dir[j][1]
#                 if (0 <= nx) and (nx < r) and (0 <= ny) and (ny < c):
#                     if arr[nx][ny] == '.' and dist[nx][ny] == False:
#                         sonic.append((nx, ny))
#                         dist[nx][ny] = True
#                     elif arr[nx][ny] == 'D':
#                         return count
#
#     return -1
#
#
# r, c = map(int, sys.stdin.readline().split())
# nl = []
#
# for i in range(r):
#     nl.append(list(sys.stdin.readline().rstrip()))
#
# o = find(nl)
#
# if o == -1:
#     print("KAKTUS")
# else:
#     print(o)

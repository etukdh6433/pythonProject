"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
19주차 2178 미로 탐색
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
#
#
# def find(arr):
#     d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     q = deque([[0, 0]])
#     visit = [[0 for _ in range(m)] for _ in range(n)]
#     visit[0][0] = 1
#
#     while q:
#         u = q.popleft()
#         for i in range(4):
#             x = u[0] + d[i][0]
#             y = u[1] + d[i][1]
#             if 0 <= x < n and 0 <= y < m:
#                 if arr[x][y] == 1 and visit[x][y] == 0:
#                     visit[x][y] = visit[u[0]][u[1]] + 1
#                     q.append([x, y])
#
#     return visit[-1][-1]
#
#
# n, m = map(int, sys.stdin.readline().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().rstrip())))
#
# print(find(graph))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
18주차 9934 완전 이진 트리
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
19주차 9934 완전 이진 트리
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# sys.setrecursionlimit(10**6)
#
#
# def cbt(arr, level):
#     mid = len(arr)//2
#     val = arr[mid]
#
#     graph[level].append(val)
#
#     if len(arr) == 1:
#         return
#
#     cbt(arr[0:mid], level + 1)
#     cbt(arr[mid + 1:len(arr)], level + 1)
#
#
# k = int(sys.stdin.readline())
# order = list(map(int, sys.stdin.readline().split()))
# graph = [[] for _ in range(k)]
#
# cbt(order, 0)
#
# for i in range(k):
#     print(*graph[i])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
19주차 1991 트리순회
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# sys.setrecursionlimit(10**6)
#
#
# n = int(sys.stdin.readline())
# graph = [[] for _ in range(n)]
# preorder = []
# inorder = []
# postorder = []
#
# for _ in range(n):
#     ro, le, ri = sys.stdin.readline().split()
#     ron = ord(ro)
#
#     graph[ron-65].append(ro)
#     graph[ron-65].append(le)
#     graph[ron-65].append(ri)
#
#
# def pre_order(grr, s=0):
#     preorder.append(grr[s][0])
#
#     if grr[s][1] != '.':
#         pre_order(grr, ord(grr[s][1]) - 65)
#
#     if grr[s][2] != '.':
#         pre_order(grr, ord(grr[s][2]) - 65)
#
#     return
#
#
# pre_order(graph)
# print(*preorder, sep='')
#
#
# def in_order(grr, s=0):
#     if grr[s][1] != '.':
#         in_order(grr, ord(grr[s][1]) - 65)
#
#     inorder.append(grr[s][0])
#
#     if grr[s][2] != '.':
#         in_order(grr, ord(grr[s][2]) - 65)
#
#     return
#
#
# in_order(graph)
# print(*inorder, sep='')
#
#
# def post_order(grr, s=0):
#     if grr[s][1] != '.':
#         post_order(grr, ord(grr[s][1]) - 65)
#
#     if grr[s][2] != '.':
#         post_order(grr, ord(grr[s][2]) - 65)
#
#     postorder.append(grr[s][0])
#
#     return
#
#
# post_order(graph)
# print(*postorder, sep='')


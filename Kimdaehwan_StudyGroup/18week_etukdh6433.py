"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
18주차 1260 DFS와 BFS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
#
# def dfs(s):
#     nl = []
#     l = [s]
#
#     while l:
#         s = l.pop()
#         if s not in nl:
#             nl.append(s)
#             l.extend(graphd[s])
#
#     print(*nl)
#
#
# def bfs(s):
#     ml = [s]
#     q = graphb[s].copy()
#
#     while q:
#         s = q.pop(0)
#         if s not in ml:
#             ml.append(s)
#             q.extend(graphb[s])
#
#     print(*ml)
#
#
# n, m, v = map(int, sys.stdin.readline().split())
# graphd = [[] for _ in range(n + 1)]
# graphb = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#
#     graphd[a].append(b); graphd[b].append(a)
#     graphd[a].sort(reverse=True); graphd[b].sort(reverse=True)
#
#     graphb[a].append(b); graphb[b].append(a)
#     graphb[a].sort(); graphb[b].sort()
#
# dfs(v)
# bfs(v)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
18주차 24479 알고리즘 수업 - 깊이 우선 탐색
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# sys.setrecursionlimit(10**6)
#
#
# def dfs(V, E, r, order):
#     V[r] = order
#     e = E[r]
#
#     for j in e:
#         if V[j] == 0:
#             order = dfs(V, E, j, order + 1)
#
#     return order
#
#
# n, m, r = map(int, sys.stdin.readline().split())
# V = [0 for _ in range(n + 1)]
# E = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     E[a].append(b)
#     E[b].append(a)
#
# for i in range(1, n + 1):
#     E[i].sort()
#
# order = 1
# dfs(V, E, r, order)
#
# for i in range(1, n + 1):
#     print(V[i])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
18주차 24479 알고리즘 수업 - 넓이 우선 탐색
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

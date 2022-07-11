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
18주차 14503 로봇 청소기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

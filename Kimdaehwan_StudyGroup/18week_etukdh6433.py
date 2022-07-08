"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
18주차 1260 DFS와 BFS (오답)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
#
# def dfs(s):
#     nl = [s]
#     while graph_d[s] != [0 for _ in range(n + 1)]:
#         i = graph_d[s].index(1)
#         if graph_d[s][i] == 1 or graph_d[i][s] == 1:
#             graph_d[s][i] = 0
#             graph_d[i][s] = 0
#             s = i
#             if s not in nl:
#                 nl.append(s)
#     print(*nl)
#     return
#
#
# def bfs(s):
#     ml = [s]
#     j = 0
#     while graph_b[s] != [0 for _ in range(n + 1)]:
#         i = graph_b[s].index(1)
#         if graph_b[s][i] == 1 or graph_b[i][s] == 1:
#             graph_b[s][i] = 0
#             graph_b[i][s] = 0
#             if i not in ml:
#                 ml.append(i)
#         if graph_b[s] == [0 for i in range(n + 1)]:
#             j += 1
#             s = j
#     print(*ml)
#     return
#
#
# n, m, v = map(int, sys.stdin.readline().split())
# graph_d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# graph_b = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#
#     graph_d[a][b] = 1
#     graph_d[b][a] = 1
#
#     graph_b[a][b] = 1
#     graph_b[b][a] = 1
#
# dfs(v)
# bfs(v)

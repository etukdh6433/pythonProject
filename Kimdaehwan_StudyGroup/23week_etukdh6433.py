"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
23주차 11725 트리의 부모 찾기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# sys.setrecursionlimit(10**6)
#
#
# def DFS(a):
#     for i in graph[a]:
#         if visit[i] == -1:
#             visit[i] = a
#             DFS(i)
#
#
# N = int(sys.stdin.readline())
# graph = [[] for _ in range(N + 1)]
# visit = [-1 for _ in range(N + 1)]
#
# for _ in range(N - 1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# DFS(1)
#
# for i in range(2, N + 1):
#     print(visit[i])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
23주차 20364 부동산 다툼
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# N, Q = map(int, sys.stdin.readline().split())
# visit = [False for _ in range(N + 1)]
#
# for _ in range(Q):
#     x = int(sys.stdin.readline())
#     s = x
#     visit_node = 0
#     c = 0
#     while s != 0:
#         if visit[s]:
#             c = 1
#             visit_node = s
#         s //= 2
#
#     if c:
#         print(visit_node)
#     else:
#         visit[x] = True
#         print(0)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
23주차 15900 나무 탈출
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# sys.setrecursionlimit(10**6)
#
#
# def DFS():
#     while stack:
#         rn, l = stack.pop()
#         visit[rn] = 1
#
#         if rn != 1 and len(graph[rn]) == 1:
#             leng.append(l)
#             continue
#
#         for i in graph[rn]:
#             if visit[i] == 0:
#                 stack.append([i, l + 1])
#
#
# N = int(sys.stdin.readline())
# graph = [[] for _ in range(N + 1)]
# visit = [0 for _ in range(N + 1)]
# stack = [[1, 0]]
# leng = []
#
# for _ in range(N - 1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# DFS()
#
# if sum(leng) % 2:
#     print('Yes')
# else:
#     print('No')

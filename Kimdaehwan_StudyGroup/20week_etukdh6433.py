"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
20주차 2583 영역 구하기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
#
# m, n, k = map(int, sys.stdin.readline().split())
# field = [[0 for _ in range(n)] for _ in range(m)]
# result = []
#
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             field[i][j] += 1
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
#             if (0 <= x < n) and (0 <= y < m) and (field[y][x] == 0):
#                 field[y][x] = 1
#                 q.append((x, y))
#                 cnt += 1
#
#     return cnt
#
#
# for i in range(m):
#     for j in range(n):
#         if field[i][j] == 0:
#             field[i][j] += 1
#             result.append(area(j, i))
#
# print(len(result))
# print(*sorted(result))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
20주차 1946 신입 사원
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
#
# def func():
#     dmi = grade[0][1]
#     cnt = 0
#
#     for i in range(n):
#         if grade[i][1] <= dmi:
#             cnt += 1
#             dmi = grade[i][1]
#
#     return cnt
#
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     grade = []
#     for _ in range(n):
#         graph = list(map(int, sys.stdin.readline().split()))
#         grade.append(graph)
#
#     grade.sort()
#
#     print(func())


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
20주차 1931 회의실 배정
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# n = int(sys.stdin.readline())
# time = []
#
# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     time.append([a, b])
#
# time.sort()
# s_time = time[-1][0]
#
# cnt = [0 for _ in range(n)]
# cnt[-1] = 1
#
# for i in range(n - 2, -1, -1):
#     if time[i][1] <= s_time:
#         s_time = time[i][0]
#         cnt[i] = cnt[i + 1] + 1
#     else:
#         cnt[i] = cnt[i + 1]
#
# print(max(cnt))

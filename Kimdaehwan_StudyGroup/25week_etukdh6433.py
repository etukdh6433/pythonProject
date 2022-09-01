"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
25주차 2156 포도주 주식
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# N = int(sys.stdin.readline())
# wine = [0]
# result = [0 for _ in range(N + 1)]
#
# for _ in range(N):
#     wine.append(int(sys.stdin.readline()))
#
#
# def sum_wine(n):
#     if n == 1:
#         result[1] = wine[1]
#
#     elif n == 2:
#         result[1] = wine[1]
#         result[2] = wine[2] + wine[1]
#
#     elif n == 3:
#         result[1] = wine[1]
#         result[2] = wine[2] + wine[1]
#         result[3] = wine[3] + max(result[1], wine[2] + result[0])
#
#     elif n >= 4:
#         result[1] = wine[1]
#         result[2] = wine[2] + wine[1]
#         result[3] = wine[3] + max(result[1], wine[2] + result[0])
#         for i in range(4, N + 1):
#             result[i] = wine[i] + max(result[i - 2], wine[i - 1] + result[i - 3], wine[i - 1] + result[i - 4])
#
#     return result
#
#
# result = sum_wine(N)
#
# print(max(result))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
25주차 15686 치킨 배달
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# field = []
#
# for _ in range(N):
#     field.append(list(map(int, sys.stdin.readline().split())))

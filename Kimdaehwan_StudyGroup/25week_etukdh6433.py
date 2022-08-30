"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
25주차 2156 포도주 주식 (오답)
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
#     elif n >= 3:
#         result[1] = wine[1]
#         result[2] = wine[2] + wine[1]
#         for i in range(3, N + 1):
#             result[i] = wine[i] + max(result[i - 2], wine[i - 1] + result[i - 3])
#
#     return result
#
#
# result = sum_wine(N)
#
# print(max(result))

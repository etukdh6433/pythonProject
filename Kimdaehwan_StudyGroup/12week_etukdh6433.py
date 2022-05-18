"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
12주차 19941 햄버거 분배
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# ham = list(sys.stdin.readline().rstrip())
# cnt = 0
#
# for i in range(n):
#     if ham[i] == 'P':
#         if i >= k and 'H' in ham[i-k:i+k+1]:
#             cnt += 1
#             for j in range(i-k,i+k+1):
#                 if ham[j] == 'H':
#                     ham[j] = 0
#                     break
#         elif i < k and 'H' in ham[0:i+k+1]:
#             cnt += 1
#             for j in range(0,i+k+1):
#                 if ham[j] == 'H':
#                     ham[j] = 0
#                     break
#
# print(cnt)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
12주차 10837 동전 게임
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# k = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# lc = []
#
# for i in range(c):
#     lc.append(list(map(int, sys.stdin.readline().split())))
#     m, n = 0, 0
#     for j in range(k):
#         r = k - j - 1
#         if m != lc[i][0]:
#             m += 1
#         if m + r < n:
#             break
#         if n != lc[i][1]:
#             n += 1
#         if n + r < m:
#             break
#     if lc[i] == [m, n]:
#         print(1)
#     else:
#         print(0)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
12주차 2512 예산
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# n = int(sys.stdin.readline())
# lo = list(map(int, sys.stdin.readline().split()))
# lo.sort()
# m = int(sys.stdin.readline())
# lo_an = [0 for i in range(n)]
#
# if sum(lo) <= m:
#     lo_an = lo
#     print(max(lo_an))
# else:
#     for i in range(n):
#         x = lo_an.count(0)
#         y = m - sum(lo_an)
#         if y//x >= lo[i]:
#             lo_an[i] = lo[i]
#         else:
#             for j in range(i,n):
#                 lo_an[j] = y//x
#             break
#
#     print(f"{max(lo_an)}")
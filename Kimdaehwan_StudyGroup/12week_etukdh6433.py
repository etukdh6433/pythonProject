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
#
# for i in range(c):
#     m, n = map(int, sys.stdin.readline().split())
#     # 두 점수의 차이
#     gap = abs(m - n)
#     # 누구도 점수를 얻지 못하는 라운드
#     r = k - max(m, n)
#
#     if m == n:
#         print(1)
#     elif m > n:
#         if gap - r <= 2:
#             print(1)
#         else:
#             print(0)
#     elif m < n:
#         if gap - r <= 1:
#             print(1)
#         else:
#             print(0)


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
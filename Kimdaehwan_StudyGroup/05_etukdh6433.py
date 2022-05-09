"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
5주차 18258 큐2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from collections import deque
#
# que = deque([])
# loop = int(sys.stdin.readline())
#
# for i in range(loop):
#     command = list(sys.stdin.readline().split())
#
#     if(command[0] == 'push'):
#         que.append(int(command[1]))
#
#     elif (command[0] == 'pop'):
#         if (len(que) == 0):
#             print(-1)
#         else:
#             print(que[0])
#             que.popleft()
#
#     elif (command[0] == 'size'):
#         print(len(que))
#
#     elif (command[0] == 'empty'):
#         if(len(que) == 0):
#             print(1)
#         else:
#             print(0)
#
#     elif (command[0] == 'front'):
#         if (len(que) == 0):
#             print(-1)
#         else:
#             print(que[0])
#
#     elif (command[0] == 'back'):
#         if (len(que) == 0):
#             print(-1)
#         else:
#             print(que[len(que)-1])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
5주차 2579 계단오르기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# def point (N):
#     if (N == 1):
#         get_point[1] = stair[1]
#
#     elif (N == 2):,
#         get_point[1] = stair[1]
#         get_point[2] = stair[2]+stair[1]
#
#     elif (N >= 3):
#         get_point[1] = stair[1]
#         get_point[2] = stair[2] + stair[1]
#         for i in range(3,N+1):
#             get_point[i] = stair[i] + max(get_point[i-2],stair[i-1]+get_point[i-3])
#
#     return get_point
#
# N = int(sys.stdin.readline())
# stair = [0]
# get_point = [0 for i in range(N+1)]
#
# for i in range(1,N+1):
#     stair.append(int(sys.stdin.readline()))
#
# get_point = point(N)
#
# print(get_point[N])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
5주차 11501 주식
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# T = int(sys.stdin.readline())
#
# for i in range(T):
#     sum_money = 0
#     day = int(sys.stdin.readline())
#     stock = list(map(int, sys.stdin.readline().split()))
#     max_value = 0
#
#     for j in range(day-1, -1, -1):
#         if (stock[j] >= max_value):
#             max_value = stock[j]
#
#         elif (stock[j] < max_value):
#             sum_money += (max_value - stock[j])
#
#     print(sum_money)
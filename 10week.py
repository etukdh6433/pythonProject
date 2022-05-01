# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 10주차 6986 절사평균
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
# score = []
#
# for i in range(N):
#     score.append(float(sys.stdin.readline())+5e-16)
#
# sort_score = sorted(score)
#
# for j in range(K):
#     sort_score[j] = 0
#     sort_score[-(j+1)] = 0
#
# print(f"{sum(sort_score)/(len(sort_score)-2*K):.2f}")
#
# for k in range(K-1,-1,-1):
#     sort_score[k] = sort_score[k+1]
#     sort_score[-(k+1)] = sort_score[-(k+2)]
#
# print(f"{sum(sort_score)/len(sort_score):.2f}")


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 10주차 2628 종이자르기
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# max_height = 0
# max_width = 0
# w, h = map(int, sys.stdin.readline().split())
# t = int(sys.stdin.readline())
# cut_hor = [0,h]
# cut_len = [0,w]
#
# for i in range(t):
#     c, n = map(int, sys.stdin.readline().split())
#     if c == 0:
#         cut_hor.append(n)
#     elif c == 1:
#         cut_len.append(n)
#
# cut_hor = sorted(cut_hor)
# cut_len = sorted(cut_len)
#
# for j in range(len(cut_hor)-1):
#     max_height = max(cut_hor[j+1]-cut_hor[j], max_height)
#
# for k in range(len(cut_len)-1):
#     max_width = max(cut_len[k+1]-cut_len[k], max_width)
#
# print(f"{max_height*max_width}")


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 10주차 2303 숫자 게임
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

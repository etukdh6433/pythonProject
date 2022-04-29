# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 10주차 6986 절사평균
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
# from decimal import Decimal
#
# N, K = map(int, sys.stdin.readline().split())
# score = []
#
# for i in range(N):
#     score.append(float(Decimal(sys.stdin.readline())))
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
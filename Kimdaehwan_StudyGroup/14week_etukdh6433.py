"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
14주차 2548 대표 자연수
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# n = int(sys.stdin.readline())
# nl = list(map(int, sys.stdin.readline().split()))
# nl.sort()
# ml = []
#
# for i in range(n//2-1, n):
#     d = 0
#     for j in range(n):
#         d += abs(nl[i] - nl[j])
#     ml.append([d, nl[i]])
#     if len(ml) > 1 and ml[len(ml)-2][0] < d:
#         break
#
# y = min(ml)
# print(f"{y[1]}")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
14주차 2304 창고 다각형 (시간 초과)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# msize = 1002
# t = int(sys.stdin.readline())
# nl = [0 for i in range(msize)]
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     nl[a] = b
#
# s = 1
# e = 1001
# s_val = 0
# e_val = 0
# mvalue_index = nl.index(max(nl))
#
# while s != mvalue_index or e != mvalue_index:
#     if s != mvalue_index:
#         if s_val != 0 and s_val > nl[s]:
#             nl[s] = s_val
#             s += 1
#         elif s_val <= nl[s]:
#             s_val = nl[s]
#             s += 1
#     if e != mvalue_index:
#         if e_val != 0 and e_val > nl[e]:
#             nl[e] = e_val
#             e -= 1
#         elif e_val <= nl[e]:
#             e_val = nl[e]
#             e -= 1
#
# print(f"{sum(nl)}")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
14주차 2641 다각형그리기 (오답)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# size = int(sys.stdin.readline())
# nl = list(map(int, sys.stdin.readline().split()))
# nl += nl
# nl_r = reversed(nl)
# ml = []
# for i in nl_r:
#     if i == 1:
#         ml.append(3)
#     elif i == 3:
#         ml.append(1)
#     elif i == 2:
#         ml.append(4)
#     elif i == 4:
#         ml.append(2)
#
# cnt = 0
# cor = []
#
# t = int(sys.stdin.readline())
#
# for i in range(t):
#     ll = list(map(int, sys.stdin.readline().split()))
#     for j in range(size):
#         if ll == nl[j:j+10]:
#             cnt += 1
#             cor.append(ll)
#             break
#         elif ll == ml[j:j+10]:
#             cnt += 1
#             cor.append(ll)
#             break
#
# print(f"{cnt}")
# for i in cor:
#     for j in i:
#         print(j, end=" ")
#     print()

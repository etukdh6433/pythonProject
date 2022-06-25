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
# n = int(sys.stdin.readline())
# roof = dict()
#
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     roof[a] = b
#
# roof = dict(sorted(roof.items()))
# key = list(roof.keys())
# value = list(roof.values())
#
# max_value_index = value.index(max(value))
# s, e = max_value_index, max_value_index
#
# while s != 0 or e != n-1:
#     if s != 0 and value[s] < value[s-1]:
#         del roof[key[s]]
#         s -= 1
#     elif s != 0:
#         s -= 1
#
#     if e != n-1 and value[e] < value[e+1]:
#         del roof[key[e]]
#         e += 1
#     elif e != n-1:
#         e += 1
#
# key = list(roof.keys())
# value = list(roof.values())
# m = len(key)
# max_value_index = value.index(max(value))
# s, e = max_value_index, max_value_index
# o = max(value)
#
# while s != 0 or e != m-1:
#     if s != 0 and value[s] >= value[s - 1]:
#         o += value[s - 1] * (key[s] - key[s - 1])
#         s -= 1
#
#     if e != m - 1 and value[e] >= value[e + 1]:
#         o += value[e + 1] * (key[e + 1] - key[e])
#         e += 1
#
# print(f"{o}")


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

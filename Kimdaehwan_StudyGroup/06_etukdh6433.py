"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
6주차 10833 사과
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# def remainApple (t):
#     #남은 사과를 저장하는 변수
#     remain = 0
#
#     for i in range(t):
#         #student = 학생 수, apple = 사과 수
#         student, apple = map(int, sys.stdin.readline().split())
#         #사과수를 학생수로 나눈 나머지 입력
#         remain += apple % student
#
#     return remain
#
# T = int(sys.stdin.readline())
#
# print(remainApple(T))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
6주차 3040 백설공주
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# dwarf = []
# sum_n = 0
#
# for i in range(9):
#     a = int(sys.stdin.readline())
#
#     if (dwarf.count(a) == 0):
#         dwarf.append(a)
#         #입력한 값의 총 합을 구한다.
#         sum_n += a
#
# for i in range(8):
#     for j in range(i+1, 9):
#         #총합 - 100과 같은 2개의 숫자 조합을 구한다. 단, 2개의 숫자중 0이 존재하면 안된다.
#         if (dwarf[i] + dwarf[j] == (sum_n - 100) and dwarf[i] != 0):
#             dwarf[i] = 0
#             dwarf[j] = 0
#
# for i in range(9):
#     if (dwarf[i] != 0):
#         print(f"{dwarf[i]}")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
6주차 1026 보물
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import sys
#
# # t대신 array를 입력받도록 해보는게 어떨지?
# def value(t):
#     value = 0
#     for i in range(t):
#         value += arr_a[i] * arr_b[i]
#
#     return value
#
# t = int(sys.stdin.readline())
# arr_a = list(map(int, sys.stdin.readline().split()))
# arr_b = list(map(int, sys.stdin.readline().split()))
#
# arr_a = sorted(arr_a,reverse=True)
# arr_b = sorted(arr_b)
#
# print(value(t))
import sys

N = int(sys.stdin.readline())
L = int(sys.stdin.readline())
bridge = [[] for i in range(L)]

ar_al = list(map(ord, sys.stdin.readline().rstrip()))

for i in range(L):
    bridge[i] = list(sys.stdin.readline().rstrip())
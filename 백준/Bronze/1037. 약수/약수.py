import sys

input = sys.stdin.readline

input()
num_list = list(map(int, input().rstrip().split()))

print(max(num_list)*min(num_list))
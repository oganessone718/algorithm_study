import sys

input = sys.stdin.readline

input()

num_list = (list(map(int, input().rstrip().split())))

print((sum(num_list)*100)/(len(num_list)*max(num_list)))
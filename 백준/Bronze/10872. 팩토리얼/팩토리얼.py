import sys

input = sys.stdin.readline

num = 1

for i in range(int(input())):
  num*=(i+1)

print(num)
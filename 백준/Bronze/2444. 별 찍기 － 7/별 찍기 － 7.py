import sys

n = int(sys.stdin.readline())

for i in range(n-1):
  print(" "*(n-1-i)+"*"*(2*i+1))
print("*"*(2*n-1))
for i in range(n-1):
  print(" "*(i+1)+"*"*(2*n-3-2*i))
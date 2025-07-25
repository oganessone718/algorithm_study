import sys

alphabets = 'abcdefghijklmnopqrstuvwxyz'
s = (sys.stdin.readline().rstrip())

for alphabet in alphabets:
  if alphabet in s:
    print(s.index(alphabet), end=" ")
  else:
    print(-1, end=" ")
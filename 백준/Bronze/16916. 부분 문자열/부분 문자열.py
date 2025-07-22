import sys

string = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

def kmp(string, pattern):
  pi = [0] * len(pattern)
  j = 0
  for i in range(1, len(pattern)):
    while j>0 and pattern[j] != pattern[i]:
      j = pi[j-1]

    if pattern[j] == pattern[i]:
      j+=1
      pi[i] = j
  
  result = []
  j = 0
  for i in range(len(string)):
    while j>0 and pattern[j] != string[i]:
      j = pi[j-1]

    if pattern[j] == string[i]:
      j+=1
      if j == len(pattern):
        j = pi[j-1]
        result.append(i-j+1)
        break
  
  if len(result)>0:
    return 1
  else:
    return 0

print(kmp(string, pattern))
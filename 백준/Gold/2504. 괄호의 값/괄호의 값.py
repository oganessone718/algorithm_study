import sys
input_string = sys.stdin.readline().rstrip()

def calculate(string):

  if len(string) == 0:
    return 0
  
  if string[0] == '(':
    left_2_cnt = 0
    right_2_cnt = 0
    for index in range(len(string)):
      if string[index] == '(':
        left_2_cnt += 1
      elif string[index] == ')':
        right_2_cnt += 1

      if right_2_cnt > left_2_cnt:
        print("0")
        exit()
      elif right_2_cnt == left_2_cnt:
        if index == 1:
          return 2+calculate(string[index+1:])
        else:
          return 2*(calculate(string[1:index]))+calculate(string[index+1:])
    if right_2_cnt != left_2_cnt:
        print("0")
        exit()
  elif string[0] == '[':
    left_3_cnt = 0
    right_3_cnt = 0
    for index in range(len(string)):
      if string[index] == '[':
        left_3_cnt += 1
      elif string[index] == ']':
        right_3_cnt += 1

      if right_3_cnt > left_3_cnt:
        print("0")
        exit()
      elif right_3_cnt == left_3_cnt:
        if index == 1:
          return 3+calculate(string[index+1:])
        else:
          return 3*(calculate(string[1:index]))+calculate(string[index+1:])
    if right_3_cnt != left_3_cnt:
        print("0")
        exit()
  else:
    print("0")
    exit()

print(calculate(input_string))
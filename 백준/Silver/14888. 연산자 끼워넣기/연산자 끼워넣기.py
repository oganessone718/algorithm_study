import sys

n, = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
operation_list = list(map(int, sys.stdin.readline().rstrip().split()))

def min_max(result_tmp, num_list_tmp, operation_list_tmp):
  if len(num_list_tmp) == 1:
    if operation_list_tmp[0] != 0:
      result = result_tmp + num_list_tmp[0]
    elif operation_list_tmp[1] != 0:
      result = result_tmp - num_list_tmp[0]
    elif operation_list_tmp[2] != 0:
      result = result_tmp * num_list_tmp[0]
    elif operation_list_tmp[3] != 0:
      if result_tmp < 0 and num_list_tmp[0] > 0:
        result = (result_tmp*(-1)//num_list_tmp[0])*(-1)
      else:
        result = result_tmp // num_list_tmp[0]
    return result, result
  else:
    min = 1000000001
    max = -1000000001
    if operation_list_tmp[0] != 0:
      min_tmp, max_tmp = min_max(result_tmp + num_list_tmp[0], num_list_tmp[1:], [operation_list_tmp[0]-1, operation_list_tmp[1], operation_list_tmp[2], operation_list_tmp[3]])
      if min_tmp < min:
        min = min_tmp
      if max_tmp > max:
        max = max_tmp
    if operation_list_tmp[1] != 0:
      min_tmp, max_tmp = min_max(result_tmp - num_list_tmp[0], num_list_tmp[1:], [operation_list_tmp[0], operation_list_tmp[1]-1, operation_list_tmp[2], operation_list_tmp[3]])
      if min_tmp < min:
        min = min_tmp
      if max_tmp > max:
        max = max_tmp
    if operation_list_tmp[2] != 0:
      min_tmp, max_tmp = min_max(result_tmp * num_list_tmp[0], num_list_tmp[1:], [operation_list_tmp[0], operation_list_tmp[1], operation_list_tmp[2]-1, operation_list_tmp[3]])
      if min_tmp < min:
        min = min_tmp
      if max_tmp > max:
        max = max_tmp
    if operation_list_tmp[3] != 0:
      if result_tmp < 0 and num_list_tmp[0] > 0:
        result = (result_tmp*(-1)//num_list_tmp[0])*(-1)
      else:
        result = result_tmp // num_list_tmp[0]
      min_tmp, max_tmp = min_max(result, num_list_tmp[1:], [operation_list_tmp[0], operation_list_tmp[1], operation_list_tmp[2], operation_list_tmp[3]-1])
      if min_tmp < min:
        min = min_tmp
      if max_tmp > max:
        max = max_tmp
    return min, max

print(min_max(num_list[0],num_list[1:],operation_list)[1],min_max(num_list[0],num_list[1:],operation_list)[0])
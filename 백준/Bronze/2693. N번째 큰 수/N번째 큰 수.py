test_case_num, = map(int, input().split())

for _ in range(test_case_num):
    num_list = list(map(int, input().split()))
    max_3rd = 0
    for _ in range(3):
        max = 0
        for num in num_list:
            if max < num:
                max = num
        max_3rd = max
        num_list.remove(max)
    print(max_3rd)
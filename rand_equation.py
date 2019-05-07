# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Copyright (c)  Baidu.com, Inc. All Rights Reserved
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
(introductions here)

argument: 
(arg1 type comment_with_example)

Authors: zhouyingfeng(zhouyingfeng@baidu.com)
Date:    //
"""

import sys
import random

# level_{numbers}_{digits_in_dec}
LVL_2_2 = 1
LVL_3_2 = 2
LVL_2_3 = 3
LVL_3_3 = 4
LVL_4_2 = 5

LVL_MAP = {
    LVL_2_2: [2, 2],
    LVL_2_3: [2, 3],
    LVL_3_2: [3, 2],
    LVL_3_3: [3, 3],
    LVL_4_2: [4, 2],
}


def _gen_equation(cnt0, cnt1):
    number_count = cnt0
    digit_count = cnt1
    num_min = pow(10, digit_count - 1)
    num_max = pow(10, digit_count) - 1
    numbers = [random.randint(num_min, num_max) for _ in range(number_count)]
    for i in range(1, number_count):
        if random.randint(0, 1) == 0:
            numbers[i] = numbers[i] * -1
    temp_result = numbers[0]
    for i2 in range(1, number_count):
        num = numbers[i2]
        if num < 0:
            if temp_result <= num_min:
                num = -int(num * 0.5)
            temp2 = temp_result + num
            while temp2 < 0:
                num = random.randint(num, -num_min)
                temp2 = temp_result + num
        else:
            if temp_result > num_max - num_min:
                num = -int(num * 0.5)
            temp3 = temp_result + num
            while temp3 > num_max:
                num = random.randint(num_min, num)
                temp3 = temp_result + num
        numbers[i2] = num
        temp_result += num
    num_strs = str(numbers[0])
    for i3 in range(1, number_count):
        num = numbers[i3]
        if num == 0:
            pass
        elif num > 0:
            num_strs += " + %d" % num
        else:
            num_strs += " - %d" % abs(num)
    return num_strs + " = " + "_" * 10


def _main():
    args = sys.argv
    # times, level
    times = 30 if len(args) <= 1 else int(args[1])
    if len(args) <= 3:
        level = LVL_2_2 if len(args) < 3 else int(args[2])
        cnt0 = LVL_MAP[level][0]
        cnt1 = LVL_MAP[level][1]
    else:
        cnt0 = int(args[2])
        cnt1 = int(args[3])
    for _ in range(times):
        print _gen_equation(cnt0, cnt1)


if __name__ == '__main__':
    _main()

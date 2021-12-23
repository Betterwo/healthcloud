# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/8 9:44

import random

def create_phone():
    # 第二位数字#在五个数中随机取一个
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    print "second",second

    #第三位数字#根据第二位的数字去第二位对应的规则
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    print "third:",third

    # 最后八位数字#在最小的八位数和最大的八位数之间随机取
    suffix = random.randint(9999999,100000000)

    #print "suffix:",suffix

    # 拼接手机号
    # return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    # for i in range(0,100,1):
    #     # 生成手机号
    #     phone = create_phone()
    #     print phone
    create_phone()
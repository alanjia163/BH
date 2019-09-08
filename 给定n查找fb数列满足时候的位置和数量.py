# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys


def get_fn_add(fnadd, fn):
    return fnadd + fn


if __name__ == "__main__":
    # # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)
    n = int(sys.stdin.readline().strip())
    # n = int(input())
    list1 = []
    my_dict = {}
    list_total = []
    for i in range(1, n):
        fn = i
        for j in range(1, n):
            fn_add = j
            list1.append(fn)
            list1.append(fn_add)
            while fn_add < n:
                fn_add_add = fn_add + fn
                fn, fn_add = fn_add, fn_add_add
                list1.append(fn_add_add)
            if n in list1:
                index = list1.index(n) + 1
                if index in my_dict.keys():
                    my_dict[index] += 1
                else:
                    my_dict[index] = 1
                list_total.append(list1)
            list1 = []
    print(list_total)
    for k, value in my_dict.items():
        print(k, ' ', value)

def string_distance(s1, s2):
    # 矩阵的下标得多一个
    len_str1 = len(s1) + 1
    len_str2 = len(s2) + 1

    # 初始化了一半  剩下一半在下面初始化
    matrix = [[0] * (len_str2) for i in range(len_str1)]

    for i in range(len_str1):
        for j in range(len_str2):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            # 初始化矩阵
            elif i == 0 and j > 0:
                matrix[0][j] = j
            elif i > 0 and j == 0:
                matrix[i][0] = i
            # flag
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
    return matrix[len_str1 - 1][len_str2 - 1]

if __name__ == '__main__':
    # a = 'FreshMeat'
    # b = 'FishAndMeat'
    a=input()
    b=input()
    result = string_distance(a, b)
    result=int(result)
    print(result)

# # a=input()
# # b=input()
# a='FreshMeat'
# b='FishAndMeat'
# min_edit_dist(a, b)  # 测试
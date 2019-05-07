# def utilityFunction(s, j):
#     s = s[:j] + s[j + 1:]
#     return s
def utilityFunction(s,j):
    # ret =[]
    # for i in range(len(s)):
    #     ret.append(-100)
    # d =0
    # for k in range(len(s)):
    #     if k == j:
    #         d =1
    #     else:
    #         ret[k-d]=s[k]
    # list_to_string_ret = ''.join(ret)#列表转字符串
    # return list_to_string_ret
    s =s[:j]+s[j+1:]
    return s
# # a,b在长度相等的条件下，判断a,b中元素是否一样
def no_name(a,b):
    if len(a) !=len(b):
        return False
    for x in range(len(b)):
        if a[0]==b[x]:
            return no_name(utilityFunction(a,0),utilityFunction(b,x))
    print(len(b)==0)
    return len(b)==0

if __name__ == '__main__':
    # print(utilityFunction(['1a', '2b', '3c', '4d', '5e','6f','7g'], 2))
    print(no_name("abcdf","abdfc"))


#



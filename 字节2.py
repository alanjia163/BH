
def solve(list_total,n):
    t =list_total[-1][0]#总时间
    value =0#当前剩余数
    sum_his =0#历史总数

    his_max=list_total[-1][1] #历史最高
    for i in range(n-1):
        sum_his =sum_his+list_total[i][1]
        if his_max < sum_his -list_total[i][0]+1:
            his_max =sum_his -list_total[i][0]+1

    value = sum_his-t
    if value>his_max:
        his_max=value
    return value+list_total[-1][1]+list_total[-1][0],his_max


if __name__ == '__main__':
    n = int(input())
    list_total=[]
    for i in range(n):
        list_total.append(list(map(int, input().split(" "))))
    print(solve(list_total,n))


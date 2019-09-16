if __name__ == '__main__':
    list1 = list(map(str, input().split(" ")))
    list2=list1[-1][:-1]
    list1 =list1[:-1]
    list1.append(list2)
    for i in range(len(list1)):
        if list1[i] !='':
            list1[i]=list1[i]+'.'
            break
    list1.reverse()
    for i in range(len(list1)):
        if list1[i] != '':
            print(list1[i], end=" ")

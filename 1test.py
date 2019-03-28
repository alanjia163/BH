def calPoints(self, ops):
    a = int(ops[0])
    list = [a]
    j = 0
    for i in range(1, len(ops)):
        k = len(list)
        if ops[i] == 'D':
            list.append(list[k - 1] * 2)
        elif ops[i] == '+':
            list.append(list[k - 2] + list[k - 1])
        elif ops[i] == 'C':
            list.pop(k - 1)
            j = j + 1
        else:
            list.append(int(ops[i]))
    a = sum(list)
    return a
print(calPoints())
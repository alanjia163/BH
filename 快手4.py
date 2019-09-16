board=[]
for i in range(9):
    str=input()
    temp=[s for s in str]
    board.append(temp)
# print(board)
def shudu(board):
    # row，col，cell分别代表行，列，3x3单元格
    row= [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    col=[{}, {}, {}, {}, {}, {}, {}, {}, {}]
    cell=[{}, {}, {}, {}, {}, {}, {}, {}, {}]

    for x in range(9):
        for y in range(9):
            # 取得单元格
            num = 3 * (x // 3) + y // 3
            temp = board[x][y]
            # 不需要存入 '.'
            if temp != 'X':
                if (temp not in row[x]
                        and temp not in col[y]
                        and temp not in cell[num]):
                    row[x][temp] = '1'
                    col[y][temp] = '1'
                    cell[num][temp] = '1'
                else:
                    return "false"
    return "true"
print(shudu(board))
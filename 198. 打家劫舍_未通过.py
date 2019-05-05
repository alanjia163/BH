def ab(nums):
    lenth = len(nums)
    if lenth < 1:
        return 0
    if record[lenth - 1]:
        return record[lenth - 1]
    record[lenth - 1] = max(nums[lenth - 1] + ab(nums[:lenth - 2]), ab(nums[:lenth - 1]))
    return record[lenth - 1]

if __name__ == '__main__':
    nums=[1,2,3,4,6,3,4,1]
    record = []
    for i in range(len(nums)):
        record.append(0)
    # return ab(nums)
    print(ab(nums))
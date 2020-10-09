def rangeCount(arr, s, e):
    count = 0
    for i in arr:
        if i >= s and i <= e:
            count += 1
    if count > (s - e + 1):
        return True
    else:
        return False


def findDup(array):
    start = 1
    end = len(array) - 1
    while end >= start:
        middle = (end-start)//2 + start
        if rangeCount(array, start, middle):
            end = middle
        else:
            start = middle
        if end == start:
            break

    count = 0
    for i in array:
        if i == start:
            count += 1
    if count >= 2:
        num = start
        print(num)
    else:
        num = end
        print(num)
    return num

array = [2,3,5,4,3,2,6,7]
findDup(array)

#print(rangeCount(array, 1, 7))
        left_sum = nums[0]
        right_sum = sum(nums[2:])
        for i in range(len(nums),2):
            left_sum = left_sum + nums[i-1]
            right_sum = right_sum - nums[i]
            if left_sum == right_sum:
                return i
        return -1

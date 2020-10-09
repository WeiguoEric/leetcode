def bubble_sort(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(nums[-1])
    return nums[-1]



def dominantIndex(nums):
    nums_ = list(nums)
    maxi = bubble_sort(nums_)
    print(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] * 2 <= maxi:
            count += 1
            print("count")
            print(count)
        if nums[i] == maxi:
            index = i
            print('index')
            print(index)
    if count == len(nums) - 1:
        return index
    else:
        return -1


arr = [0,0,2,3]

print(dominantIndex(arr))
#print(arr)



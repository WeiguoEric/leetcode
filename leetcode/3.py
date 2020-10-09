def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    #if len(nums) == 1:
        #return 1
    index = 0
    while True:
        if nums[index] == nums[index + 1]:
            print(nums[index + 1])
            nums.pop(index + 1)
        else:
            index += 1
        if index == len(nums) - 1:
            break
    print(nums)
    return len(nums)

nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums))

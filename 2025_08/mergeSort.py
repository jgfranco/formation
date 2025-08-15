def merge_sort(nums):
    if len(nums) > 1:
        leftArray = nums[:len(nums)//2]
        rightArray = nums[len(nums)//2:]

        #recursive calls

        merge_sort(leftArray)
        merge_sort(rightArray)

        #merge

        i = j = k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                nums[k] = leftArray[i]
                i += 1
            else:
                nums[k] = rightArray[j]
                j += 1
            k += 1
        
        while i < len(leftArray):
            nums[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            nums[k] = rightArray[j]
            j += 1
            k += 1

    return nums  

print(merge_sort([])) # []
print(merge_sort([1])) # [1]
print(merge_sort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(merge_sort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]


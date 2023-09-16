def sortArray(nums):
  
  for idx in range(len(nums)):
    minimum  = idx

    for j in range(idx+1, len(nums)):
      if nums[j] < nums[minimum]:
        minimum = j
    
    if minimum != idx:
      nums[idx], nums[minimum] = nums[minimum], nums[idx]
  
  return nums

# tests

print(sortArray([5,4,3,8,4,6,1]))
print(sortArray([3,2,1]))
print(sortArray([3,3,3]))
print(sortArray([1,2,3]))

    
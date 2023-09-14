def sortArray(nums):
  for j in range(0, len(nums)-1):
    iMin = j
            
    for i in range(j+1, len(nums)):
      if(nums[i] < nums[iMin]):
        iMin =i
            
    if(iMin != j):
      nums[j], nums[iMin] = nums[iMin], nums[j] 
  return nums


print(sortArray([5,3,7,1]))
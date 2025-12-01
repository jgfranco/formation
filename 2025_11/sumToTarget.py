# sum to target


def sumToTarget(nums, target):

    values = {}
    for i, num in enumerate(nums):
        values[num] = i
    

    for i, num in enumerate(nums):
        b = target- num
        if b in values: 
            return[i, values[b]]
        
    

        





print(sumToTarget([2,7, 8, 12], 9))
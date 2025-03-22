"""
https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

"""

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
        
    '''
    [0,0,1]

    traverse the whole array:

    if at i theres a zero and if at i-1 and i +1 theres a 
    zero, it means that I can place a flower:
        turn array at i into a 1 
        deduct n by 1

    I have to take care of the edges of the array so I dont go out
    of bounds

    If by the end of the traversal n is 0, we managed to place all
    the flowers, return True. Otherwise return False

    '''

    for i in range(len(flowerbed)):
        leftOpen = False
        rightOpen = False
        if flowerbed[i] == 0:
            if i > 0 and flowerbed[i-1] ==0:
                leftOpen = True
            elif i == 0: leftOpen = True
            
            if i < len(flowerbed) - 2 and flowerbed[i+1] == 0:
                rightOpen = True
            elif i == len(flowerbed) -1: rightOpen = True

            if leftOpen and rightOpen:
                flowerbed[i] = 1
                n -=1
    
    return n <= 0


print(canPlaceFlowers([1,0,0,0,0,0,1], 2)) # True
print(canPlaceFlowers([1,0,0,0,1], 1)) # True
print(canPlaceFlowers([1,0,0,0,1], 2)) # False
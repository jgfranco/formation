'''
At a large party, we have many cakes of various sizes. We want to give all of the attendees the largest possible slice we can, but also make sure all of the slices are the same size. 
The cakes are all long and rectangular like a [Jelly Roll](https://www.kingarthurbaking.com/recipes/jelly-roll-recipe), therefore each cake is represented by a single number indicating it's length.

Given an array of cake sizes and number of attendees, what is the largest piece of cake we can give each person. We want to give each person one whole piece of cake, not two that add up to the given size. Any leftover portions of cake can be used to make cake pops!
 

EXAMPLE(S)
For cakes [5, 2, 7, 4, 9] and 5 attendees, the largest slice we can cut is 4.
- We can cut one slice of size 4 from the first cake with some leftover.
- We don't use the second cake.
- We can get one slice out of the third and fourth cakes.
- The final cake of size 9, we can cut two slices.
- If we tried to cut slices of size 5, we can only make three from the cakes of length 5, 7, and 9 so 4 is the best we can do.

For cakes [1, 2, 3, 4, 9] and 6 attendees, the largest slice we can cut is 2.
- We can't use the first cake, but can get one slice out of the next 2.
- The cake of size four we can divide in half to get two slices.
- We can get four slices out of the cake of length 9.


cakes [5, 2, 7, 4, 9] and 5 attendees
    l = 1
    r = 9

    4,1      4,3  4  4,4,1

    9%4 = 1 residue
    9//4 = 2 slices
    27 //5 = slice size 5


cakes [1, 2, 3, 4, 9] and 6

get the size of the super cake 
get the potential slice size (divide super cake size betweeen attendees)

FUNCTION SIGNATURE
function maxSliceSize(cakes, attendees)
def max_slice_size(cakes, attendees):

'''

def max_slice_size(cakes, attendees):

    supercake = sum(cakes) #27
    sliceSize = supercake // attendees # 5

    slices = 0 
    while sliceSize> 0:
        for cake in cakes:
            slices +=  cake // sliceSize
        if slices >= attendees: return sliceSize
        sliceSize -=1
        slices = 0

    return sliceSize
        

# cakes [5, 2, 7, 4, 9] and 5 attendees 
        #1,  0 ,1, 0, 1

print(max_slice_size([5, 2, 7, 4, 9], 5), "expect 4")
print(max_slice_size([1, 2, 3, 4, 9], 6))

print(max_slice_size([5, 2, 7, 4, 9], 5))  # Output: 4
print(max_slice_size([1, 2, 3, 4, 9], 6))  # Output: 2
print(max_slice_size([1, 2, 3, 4, 9], 5))  # Output: 3
print(max_slice_size([8, 4, 2, 6, 1, 2, 1, 7], 14))  # Output: 2
print(max_slice_size([4, 9, 4, 3, 6, 6, 2, 5, 8, 7, 6], 13))  # Output: 3
print(max_slice_size([5, 4], 10))  # Output: 0

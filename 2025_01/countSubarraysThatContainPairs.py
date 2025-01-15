"""
subarraysSumToK(array, m, k)

————————————————————————
Eng Method
————————————————————————
# Explore 🔍

# Brainstorm 🧠


# Plan & Implement 📆

initialize:
number complement dictionary
pair count to 0
total to 0

left = 0
loop right pointer for 0 to end of array
  add right pointer complement to dictionary
  update pair count

  if range is less than m continue

  remove left pointer and increment left
  update pair count

  check if pair count is greater than 0, if so increment total

return total



[2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output is 5.

2, 4, 7, 5, 3, 5, 8, 5, 1, 7
0  0  0  0  1  2  1  1  1  0


"""

def subarraysSumToK(array, m, k):
    d = {}
    left = 0
    right = 0
    pairs = 0
    total = 0

    for right, rightValue in enumerate(array):
        print(right, rightValue)
  
        if rightValue in d:
          pairs +=1

        d[k-rightValue] = d.get(k-rightValue, 0) + 1
  

        if right - left >= m:
          print('trest')
          leftValue = array[left]
          if d[k-leftValue]:
            pairs -=1

          
      
          d[k-leftValue] -= 1
          if d[k-leftValue] == 0:
            del d[k-leftValue]
          
          
            
          left +=1
        
        

          if pairs >0: total +=1
        print(array[left:right+1])
        print(d)
        print("pairs: " , pairs)
        print("__________")

    return total

print(subarraysSumToK([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10))
            


"""
2, 4, 7, 5, 3, 5, 8, 5, 1, 7

2, 4, 7, 5 -> pairs 0
4, 7, 5, 3 -> pairs 1
7, 5, 3, 5 -> pairs 2
5, 3, 5, 8 -> pairs 1
3, 5, 8, 5 -> pairs 1
5, 8, 5, 1 -> pairs 1
8, 5, 1, 7 -> pairs 0
"""
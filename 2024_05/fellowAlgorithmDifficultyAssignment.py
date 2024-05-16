def assignAlgorithms(fellows: list[int]) -> list[int]:
  res = [1] * len(fellows)
  for i in range(1,len(fellows)):
    if fellows[i] > fellows[i-1]:
      res[i] = res[i - 1] + 1
    elif fellows[i] == fellows[i-1]:
      res[i] = res[i - 1]

  #print(res)
  for j in range(len(res)-2, -1, -1):
    if fellows[j] > fellows[j+1] and res[j]<= res[j+1]:
      res[j]  = res[j+1] + 1
    elif fellows[j] == fellows[j+1] and res[j]<= res[j+1]:
      res[j] = res[j+1]
    
  return res
    

print(assignAlgorithms([10,20,60,70,50,10,20]) 
== [1,2,3,4,2,1,2])
print(assignAlgorithms([]) == None or assignAlgorithms([]) == [])
print(assignAlgorithms([100]) == [1])
print(assignAlgorithms([11,22]) == [1,2])
print(assignAlgorithms([22,11]) == [2,1])
print(assignAlgorithms([20,20]) == [1,1])
print(assignAlgorithms([20,20,5]) == [2,2,1])
print(assignAlgorithms([5,20,20]) == [1,2,2])
print(assignAlgorithms([19,29,39]) == [1,2,3])
print(assignAlgorithms([37,27,17]) == [3,2,1])
print(assignAlgorithms([10,20,100,70,100,10,20]) == [1, 2, 3, 1, 2, 1, 2])
print(assignAlgorithms([32,22,12,22,32]) == [3,2,1,2,3])
print(assignAlgorithms([15,25,35,25,15]) == [1,2,3,2,1])
print(assignAlgorithms([15,10,25,25,25,10,15]) == [2,1,2,2,2,1,2])


def powerSet(array):
  output = []
  
  def backtracking(pointer, currentSet):
    if pointer == len(array):
      output.append(currentSet)
      return

    arr = list(currentSet)
    arr.append(array[pointer])
    backtracking(pointer+1, arr)
    backtracking(pointer+1, list(currentSet))

  backtracking(0, [])

  return output


# print(powerSet([]))
# print(powerSet(['a']))
# print(powerSet(['a','b']))
# print(powerSet(['a','b', 'c']))


def powerSet2(array):
  results = []
  subset = []

  def dfs(index):
    if index == len(array):
      results.append(list(subset))
      return
    
    dfs(index+1)
    subset.append(array[index])
    dfs(index+1)
    subset.pop()

  dfs(0)
  return results

print(powerSet2(['a', 'b']))
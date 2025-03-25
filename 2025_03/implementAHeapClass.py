
class MinHeap:
  def __init__(self):
    self.heap = []
  
  def peek(self):
    if len(self.heap) > 0:
      return self.heap[0]
    
    return None

  def size(self):
    return len(self.heap)
  
  def add(self, value):
    self.heap.append(value)
    self.bottomUp(self.size() -1)

  def getParent(self, index):
    return (index -1) //2

  def remove(self):
    minValue = self.peek()

    if minValue:
      self.swap(0, self.size()-1)
      self.heap.pop()
      self.topDown(0)

    return minValue


  def swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def bottomUp(self, index):
    parent = self.getParent(index)
  
    if parent >=0  and self.heap[index] < self.heap[parent]:
      self.swap(index, parent)
      self.bottomUp(parent)
  
  def topDown(self, index):
    leftChild = (index * 2) + 1
    rightChild = (index * 2) + 2

    smallest = index

    if leftChild < len(self.heap) and self.heap[leftChild] < self.heap[smallest]:
      smallest = leftChild
    if rightChild < len(self.heap) and self.heap[rightChild] < self.heap[smallest]:
      smallest = rightChild

    if smallest != index:
      self.swap(index, smallest)
      self.topDown(smallest)

  def toString(self):
    print(str(self.heap))

h = MinHeap();
h.add(3)

print(h.peek()) # 3
h.add(2)
print(h.peek()) # 2
print(h.remove()) # 2
print(h.peek()) # 3
h.add(4)
h.add(1)
h.add(5)
print(h.peek()) # 1
h.toString()
h.add(0)
h.toString()

# https://www.geeksforgeeks.org/binary-heap/
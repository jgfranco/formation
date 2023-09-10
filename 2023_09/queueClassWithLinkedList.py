
'''
❓ PROMPT
Implement a basic queue class using a linked list as the underlying storage. 
Queues have two critical methods, enqueue() and dequeue() to add and remove 
an item from the queue, respectively. You'll also need a constructor for your 
class, and for convenience, add a size() method that returns the current size 
of the queue. All of these methods should run in O(1) time!

Remember, a queue is a first-in, first-out (or last-in, last-out) data structure!

A doubly linked list is one of the simplest ways to implement a queue. You'll 
need both a head and tail pointer to keep track of where to add and where to 
remove data. Using a doubly linked list means you can do both operations without 
walking the whole list and all modifications of the list are at the ends.

Example(s)
q = new LLQueue();
console.log(q.size()) // 0
q.enqueue(2);
q.enqueue(3);
console.log(q.size()) // 2
console.log(q.dequeue()); // 2
console.log(q.size()) // 1
console.log(q.dequeue()); // 3
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
'''
class LLNode:
  def __init__(self, value, next = None, prev = None):
    self.value = value;
    self.next = next;
    self.prev = prev;

class LLQueue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def enqueue(self, newValue):
    newNode = LLNode(newValue)
    if self.size == 0:
      self.head = newNode    
      self.tail = newNode
      self.size +=1
      return

    self.tail.next = newNode
    prev = self.tail
    self.tail = self.tail.next
    self.tail.prev = prev
    self.size +=1

  def dequeue(self):
    # theres only one node
    if self.size == 1:
      value = self.tail.value
      self.size -=1
      self.head = None
      self.tail = None
      return value
    # two nodes or more
    elif self.size >= 2: 
      value = self.tail.value
      self.tail = self.tail.prev
      self.tail.next = None
      self.size -= 1
      return value

  def size(self):
    return self.size
  
  def __str__(self) -> str:
    if self.size ==0: return "<empty queue>"
    string = []
    curr = self.head
    while curr: 
      string.append(str(curr.value))
      curr = curr.next

    return "->".join(string)
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

q = LLQueue()
print(q.size())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q)
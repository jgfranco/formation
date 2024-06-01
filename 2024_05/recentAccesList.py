"""
Design a structure to efficiently manage a data set in order of access. The most recently accessed data is always at the end. The data least recently accessed is at the beginning.

This data structure should be implemented as a class. The constructor takes the data in the form of an array and initializes the instance.

This class must also support a fetch method that takes an ordinal (one based index) and returns the data at that position, but it also moves it to the end, due to it being accessed. For example, if the data is initially [5, 7, 3], and we access the 1st value, 5 is returned and afterward the data will be [7, 3, 5]. If then we access the 3rd value, the 5 is again returned but the order is unchanged since the 5 was already at the end.
 

EXAMPLE(S)
const q = new MRQueue([5, 7, 3]);
console.log(q.fetch(1)); // returns 5
console.log(q.fetch(1)); // returns 7
console.log(q.fetch(3)); // returns 7
 
1 2 3 
0 1 2 

4
0


Brainstorm:

- operates like a queue data strucutre
- underlying data data strucuture would be an array
- ordinal (1 indexed) -> convert to a zero based index in order to access elements
- when accessing element
- queue is reshuffled and the accessed element get placed at the end of the queue
- could be 


[1,2,3,4,5,6,6,7,8,4,3,3454346,23,4,1,2,3512,351]
|          |         |        |         |       |



Halving:
[1,2,3,4,5,6,6,7,8,4,3,345,4346,23,4,1,2,3512,351]
                        |
 ^                   length/2

_x____ groups of ___y__ elements per group 
N total elements in the input
N=x*y


remove 1 from first half
shift 345 for second half, push to first
push 1 to the end the second half


[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
|       |       |          |
  b1        b2      b3        b4    -> queues
 
                [9,10,11,12]

constructor
  - for each sqrt(n) elements, initialize a queue
  - store the queues somehow where they are ordered

fetch 3
find the bucket 3 is in

.remove on b1 -> sqrt(n) runtine

shifting from following buckets: sqrt(n) buckets
  - shift 5 from b2, push to b1 [1,2,4,5]   shifting/pushing O(1)
  - shift 9 from b3, push to b4 [6,7,8,9]
  ....

push 3 on to the last bucket (b4) O(1)

FUNCTION SIGNATURE
class MRQueue {
  constructor(data)
  fetch(ordinal)
}

class MRQueue:
  __init__(self, data):
  fetch(ordinal):

class LLnode:
  def __init__(self):
    pass

class LLlist:
  def __init__(self,head,tail):
    self.head = head
    self.tail = tail
  def add():
    pass

class MRQueue:
  def __init__(self,array):
    self.buckets, self.length = get_buckets() # array of LL
    
  def get_buckets(self):
    pass
  
  def fetch(self,index):
    bucket_number, bucket_index = divmod(index,self.length)
    
    target_bucket_head = self.bucket[bucket_number]
    
    for _ in range(bucket):
      target_bucket_head = target_bucket_head.next
    
    # shift all other buckets
    self.shift_buckets()
    return target_bucket_head.val
  
  def shift_buckets(self):
    pass


    

array_1 = [1,2,3,4,5]
MRqueue_1 = MRQueue(array_1)

Javascript Land

class MRQueue {
  constructor(data) {
    // data is an array
    // initial bucketLength = Math.ceil(Math.sqrt(data.length));
    // an array of buckets of length 
    const buckets = [];
    
    // transform data array to populate the buckets
    for (let i = 0 ; i < data.length; i++) {
      // for each element of data
      // figure out which bucket if belong to
      // add it to the bucket
    }  

    this.buckets = buckets; 

    }

  fetch(ordinal) {
    // calculate which bucket that ordinal is in
    // index = oridinal - 1

    this.balance(index) 
  }

  balance(index) {

  }
}
"""
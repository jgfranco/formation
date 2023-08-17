"""
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be solution(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.



For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be solution(queryType, query) = 6.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 4}
3 query: answer is 4
4 query: {1: 4, 2: 3}
5 query: {2: 4, 3: 3}
6 query: {2: 3, 3: 2}
7 query: answer is 2
The sum of the results for all the get queries is equal to 4 + 2 = 6.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string queryType

Array of query types. It is guaranteed that each queryType[i] is either "addToKey", "addToValue", "get", or "insert".

Guaranteed constraints:
1 ≤ queryType.length ≤ 105.

[input] array.array.integer query

Array of queries, where each query is represented either by two numbers for insert query or by one number for other queries. It is guaranteed that during all queries all keys and values are in the range [-109, 109].

Guaranteed constraints:
query.length = queryType.length,
1 ≤ query[i].length ≤ 2.

[output] integer64

The sum of the results for all get queries.
"""

def hasMapSupport(queryType, query):

    map = {}
    p = 0
    get = 0
    for i, qt in enumerate(queryType):
        print(map)
        q = query[i]
        if qt == "insert":
            map[q[0]] = q[1]
        elif qt== "addToValue":
            for k,v in map.items():
                map[k] = v + q[0]
        elif qt == "addToKey":
            #toDelete = []
            toAdd = []
            for k,v in map.items():
                toAdd.append((k+q[0], v))
                #toDelete.append(k)
            map = {} 
            for key,value in toAdd:
                map[key] = value
            
            
        elif qt == "get":
            get +=  map.get(q[0], 0)
            
    return get
queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] 
query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]
print(hasMapSupport(queryType, query))

"""Given a string array chars and an integer k, return an array of the k most frequent elements in descending order of frequency. If there is no difference in frequency, we should default to the order in which the elements originally appeared.

eg: ['a', 'b', 'a', 'b', 'b', 'c'], k = 2 => ['b', 'a'].

In this case b has a frequency of 3, so it's first. a has a frequency of 2, so it comes second. And so on.

You may use your language's built-in sorting function for convenience.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.char chars

[input] integer k

[output] array.char"""


def solution(chars, k):

    charMap = {}
    for char in chars:
        charMap[char] = charMap.get(char, 0) + 1
    
    
    sortedChars = sorted(charMap.items(), key = lambda x: x[1], reverse= True)
    
    print(sortedChars)
    result = []
    if k >len(sortedChars):
        k = len(sortedChars)
    for i in range(k):
        char, freq = sortedChars[i]
        result.append(char)
    return result


"""Q. Given an unsorted array, return the number of duplicate elements.

Examples:
Input1: []
Output1: 0
Input2: [3, 1, 1, 2, 3, 1, 1, 1, 4]
Output2: 2 // [1, 3]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] integer

the number of duplicate elements"""

def solution(array):
    
    numMap = {}
    
    for num in array:
        numMap[num] = numMap.get(num, 0) + 1
        
    repeated = filter(lambda x: x != 1, numMap.values())  
    
    return len(list(repeated))    


"""Given an array of strings, count the number of unique values.
Assume that the strings are all lowercase letters and are at least 1 character long.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string words

The array of strings

[output] integer

The number of unique words
"""
def solution(words):
    
    wordMap = {}
    for word in words:
        wordMap[word] = wordMap.get(word, 0) +1
        
  
    return len(wordMap)

"""
All squares are rectangles, but not all rectangles are squares.

You're given two strings, squares and rects, where each character represents a rectangle. The characters in squares are squares. Return the number of squares in rects.

Letters are case-sensitive, so "a" is considered a different type of rectangle from "A".
"""
def solution(squares, rects):
    squaresMap = {}
    
    for s in squares:
        squaresMap[s] = squaresMap.get(s, 0) + 1
        
    count = 0
    
    for r in rects:
        if r in squaresMap:
            count +=1
            
    return count

'''
Imagine you work at a company like Google, Facebook, OpenAI or any other company with a major online service. Millions to potentially billions of people are counting on your service to be up and running and accessible. It's an interesting thought exercise just to estimate the number of individual HTTP requests made to one of these services in a single day or even per second!

One key component of these systems is to ensure that no user can consume more than their fair share of the system's capacity to respond to these requests. This is accomplished via rate limiting, restricting the rate at which any single user can make requests.

The goal of the rate limiter is to make sure humans who use the system are able to do so, while scripts and other automatic processes might be slowed down or even denied access to reserve enough capacity for real users.

A rate-limiting algorithm (or heuristic) tracks the rate of requests from any single user and decides to allow the request through or deny it.

Work with your fellows to derive, implement, and test multiple rate-limiting algorithms. Discuss the pros and cons of each along the way.

Design these rate limiters in a testable way. We recommend passing in the current time as an argument along with the user id. The time can be a number representing seconds or milliseconds.
 

EXAMPLE(S)
console.log(isRateLimited('spammy', 1)); // false, not limited, allowed through
for (let i = 0; i < 1000; i++) isRateLimited('spammy', 1); // make a lot of calls at the same time
console.log(isRateLimited('spammy', 1)); // true, limiter kicks in, request is denied
console.log(isRateLimited('other', 1)); // false, this other user is allowed through!

// simulate waiting a long time by increasing the current time
console.log(isRateLimited('spammy', 1000000)); // false
 

FUNCTION SIGNATURE
function isRateLimited(userID: string, currentTime: number): boolean


define a threshold 

keep track of last time the user accessed the server

params:
  exposed:
    str: username
    int: time in seconds (epoch time?)
  
  internal:
    time threshold
    requests threshold
  
    
  0 ------- 60

  
  {
    lastAccessed: time       - last time of an accepted request
    numberOfRequests: int    - number of accepted requests before reset
  }

  

  currentTime - lastAccessed > 60

@ time = 0 user1 makes 300 requests -> 290 
  lastAccessed: None -> 0
  rate limited
@ time = 50, user1 makes 1 request
  lastAccessed: 0 -> 0
  still ratelimited, sinces 50 - 0 < 60
  total requests are 10
@ time 100, user1 makes 1 request
  lastAccessed: 0 -> 100
  still ratelimited, sinces 50 - 0 < 60
  is it rate limited or not?
  total requests 1
  since 100-0 >60, reset number of requests


  Plan:
  - create object with keys for users, and values of 
  {
    lastAccessed: time       - last time of an accepted request
    numberOfRequests: int    - number of accepted requests before reset
  }
  define limit
  
  getUserData(user) => {
    hashmap
  }

  rateLimit(userID, currentTime):
    - if userID isn't in database/hashmap, add it
    - if currentTime - userID.lastAccessed > 60
      - make lastAccessed = currentTime
      - numberOfRequests = 1
      - return true
    - else
      - if numberOfRequests > limit, return false
      - if numberOfRequests < limit, update numberOfRequests+=1, return true


const users = new Map();

function rateLimit(userID, currentTime) {
  if (!users.has(userID)) {

    let obj = {
      lastVisitedTime: currentTime,
      totalRequests:1
    };
    users.set(userID, obj);
    return true
  }
  

}

'''


class RateLimit:
  def __init__(self, requestLimit, timeTreshold) -> None:
    self.users = {}
    self.requestLimit = requestLimit
    self.timeTreshold = timeTreshold

  def isRateLimited(self, userId, currentTime):
    if userId not in self.users:
      self.users[userId] = (currentTime, 1)
      return True
    lastTimeAccesed = self.users[userId][0]
    totalRequests = self.users[userId][1]
    print(currentTime, lastTimeAccesed, self.requestLimit)
    if currentTime - lastTimeAccesed >= self.timeTreshold:
      self.users[userId] = (currentTime, 1)
      return True
    else:
      if totalRequests >= self.requestLimit:
        return False
      else:
        self.users[userId] = (lastTimeAccesed, totalRequests+1)
        return True

rl = RateLimit(10,60)

for _ in range(30):
  print(rl.isRateLimited("spammy", 1))

print(rl.isRateLimited("spammy",60 ))



# Second session with Martin Murjas

'''
Imagine you work at a company like Google, Facebook, OpenAI or any other company with a major online service. Millions to potentially billions of people are counting on your service to be up and running and accessible. It's an interesting thought exercise just to estimate the number of individual HTTP requests made to one of these services in a single day or even per second!

One key component of these systems is to ensure that no user can consume more than their fair share of the system's capacity to respond to these requests. This is accomplished via rate limiting, restricting the rate at which any single user can make requests.

The goal of the rate limiter is to make sure humans who use the system are able to do so, while scripts and other automatic processes might be slowed down or even denied access to reserve enough capacity for real users.

A rate-limiting algorithm (or heuristic) tracks the rate of requests from any single user and decides to allow the request through or deny it.

Work with your fellows to derive, implement, and test multiple rate-limiting algorithms. Discuss the pros and cons of each along the way.

Design these rate limiters in a testable way. We recommend passing in the current time as an argument along with the user id. The time can be a number representing seconds or milliseconds.
 

EXAMPLE(S)
console.log(isRateLimited('spammy', 1)); // false, not limited, allowed through
for (let i = 0; i < 1000; i++) isRateLimited('spammy', 1); // make a lot of calls at the same time
console.log(isRateLimited('spammy', 1)); // true, limiter kicks in, request is denied
console.log(isRateLimited('other', 1)); // false, this other user is allowed through!

// simulate waiting a long time by increasing the current time
console.log(isRateLimited('spammy', 1000000)); // false
 

FUNCTION SIGNATURE
function isRateLimited(userID: string, currentTime: number): boolean


Approach 1: Sliding Window
 
Map1: {
  userName1: [timestamp3, timestamp4]
  userName2: [timestamp1, timestamp2, timestamp3, timestamp4]
  userName3: [timestamp1, timestamp2, timestamp3, timestamp4]
  userName4: [timestamp1, timestamp2, timestamp3, timestamp4]
}

Map2: {
  userName1: [timestamp1, timestamp2, timestamp3, timestamp4]
  userName2: [timestamp1, timestamp2, timestamp3, timestamp4]
  userName3: [timestamp1, timestamp2, timestamp3, timestamp4]
  userName4: [timestamp1, timestamp2, timestamp3, timestamp4]
}

threshold = 4
timeframe = 300

time: 302

5 -> 8 -> 295 -> 302


Approach 2: Fixed Window Counter


timeframe = 300 
allowedRequests = 50

  t   r  
  3 - 49
  4 - 0
  5 - 50

  8
  10
  2
  301 - 1 => should be allowed
  305

Map: {             601                1
  userName1: (lastTimeStamp, #ofRequests)
}


Approach 3: Token Bucket 


bucket size: 50 tokens
refill rate: 50 tokens per 300s
refill rate: adds 1 token per second

request => check bucket for tokens, if yes decrement token
  if no, reject request


Approach 4: Leaky Bucket Approach
leak rate => 1 request per second

build a queue with requests => go through at leak rate


'''


''' JAVASCRIPT solutions 
// Sliding Window
let requestCounts = {}; // id -> count
const MAX_REQUESTS = 3;
const INTERVAL = 10;
let lastWindowStart = 0;

function isRateLimitedSlidingWindow(id, t) {
  if (t - lastWindowStart > INTERVAL) {
    lastWindowStart = t;
    requestCounts = {};
  }
  
  requestCounts[id] = (requestCounts[id] || 0) + 1;
  
  return requestCounts[id] > MAX_REQUESTS;  
}

// Token Bucket
const MAX_TOKENS = 3;
const TOKEN_INTERVAL = 10; // tokens += 1 every 10 ms

const tokens = {}; // id -> { count, lastFilled }

function isRateLimitedTokenBucket(id, t) {
  if (!tokens[id]) {
    tokens[id] = { count: MAX_TOKENS, lastFilled: t };
  }
  
  if (tokens[id].count <= 0) {
    tokens[id].count = Math.min(
      Math.floor((t - tokens[id].lastFilled) / TOKEN_INTERVAL),
      MAX_TOKENS
    );
    tokens[id].lastFilled = t;
  }
  
  const isLimited = (tokens[id].count <= 0);

  if (!isLimited) {
    tokens[id].count -= 1;
  }
  
  return isLimited;
}
'''
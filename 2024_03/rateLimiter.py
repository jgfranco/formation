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


BRAINSTORMING

1. Allow n (e.g., 1000) requests per time window per user (e.g., 1h).  Keep track of request count per user during a window.  Don't permit anything over n during that window.  Count resets for that user after a cooldown threshold (regardless of the window size). O(1) / O(u)
    - How does the remaining requests get reset?
    - Does the cooldown change with multiple violations?
2. Track the timestamps of each user access in a queue, discard events that are sufficiently old.  Deny access when the queue is too long.
    a. O(r) / O(r * u) expect is much less than r * u... closer to just u -- discard all old stuff
    b. O(1) / O(r * u) expected is pretty much the worst case all the time -- discard single item when full
3. Always allow initial request.  Keep track of most recent timestamp per user.  Only allow new requests if more than n ms have passed since the last request. O(1) / O(u)
4. Allow n requests for all users per time window, refuse all requests from any user if the capacity is used up.  Numbers all reset at the start of the next time window. O(1) / O(1)
5. Allow first request always.  Delay responding to subsequent requests for a given user until n ms have passed since the last permitted request.
6. Each user gets n "tokens" per time period (e.g., 1000 per day).  Each passing request uses up a token.  Tokens regenerate at a certain pace (41 / h).  Requests made when no tokens are available are refused.  There is a max of 5 x daily limit tokens.


GOALS:

- Give everyone a fair chance to access the system
    - Prevent robots from monopolizing resources at the expense of human users
- Prevent bad actors from burning up our resources
- Prevent DDOS attacks
- Prevent too many (even legit) requests from tanking our systems
- Encourage premium subscribers
- 


OPEN QUESTIONS:

- Is there an upper bound of total requests per time period?  Should we block everyone if we've exceeded that amount?
- Is it okay to simply drop requests altogether?
- Are we trying to completely prevent bots?


'''
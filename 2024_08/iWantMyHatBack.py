'''
❓ PROMPT
Oliver the Dog is missing his favorite hat and is asking his friends at 
the dog park if they've seen it. Each dog either has seen it or suggests 
a list of other dogs to ask. Return the name of the dog who has seen the 
hat. Oliver starts out by asking his best friend. This function will 
take two parameters. The first is a map of dogs to a list of their 
friends. The second is Oliver's best friend, who Oliver will ask first.

One of the most common uses of a queue is to keep a list of "work to be 
done". Just like doing housework, often new things get added to the to-do
list while doing some other task. New jobs get added to the end of the 
queue, and when one is complete, the next one is taken from the top of 
the list.

As a follow-up, how would you handle it when there's circular knowledge? 
For example, Jono's suggestion is to ask Angus, and Angus' suggestion is 
to ask Jono. These 'cycles' aren't restricted to pairs of dogs, they can 
be of any size.

Example(s)
dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], // Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
}
findHat(dogs, 'Loki') == 'Ivy'
 

🔎 EXPLORE
List your assumptions & discoveries:
1. use visited set to avoid infinite loops in the presence of cycles

Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1: use a queue to visit all the dogs, use a visited set to avoid loops
Time: O(n) where N is the number of dogs
Space: O(n) 
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function findHat(dogs, bestFriend) {
def findHat(dogs: dict, bestFriend: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def findHat(dogs, bestFriend):
  from collections import deque
  q = deque([bestFriend])
  visited = set()
  while q:
    dog = q.popleft()

    if dog in visited: continue 
    visited.add(dog)
    for friend in dogs[dog]:
      if friend == "HAT":
        return dog
      q.append(friend)

  return "Couldn't find the hat"


dogs = {
    'Carter': ['Fido', 'Ivy'],
    'Ivy': ["HAT"], # Ivy has seen the hat
    'Loki': ['Snoopy'],
    'Pepper': ['Carter'],
    'Snoopy': ['Pepper'],
    'Fido': []
}
print(findHat(dogs, 'Loki') == "Ivy")
print(findHat(dogs, 'Snoopy') == "Ivy")
print(findHat(dogs, 'Ivy') == "Ivy")
print(findHat(dogs, 'Fido') == "Couldn't find the hat")

dogs = {
    'Ariel': ['Bork'],
    'Bork': ['Cassie'],
    'Cassie': ['Drex'],
    'Drex': ['Zoe'],
    'Zoe': ["HAT"],
}
print(findHat(dogs, "Ariel") == "Zoe")
print(findHat(dogs, "Bork") == "Zoe")
print(findHat(dogs, "Cassie") == "Zoe")
print(findHat(dogs, "Drex") == "Zoe")
print(findHat(dogs, "Zoe") == "Zoe")
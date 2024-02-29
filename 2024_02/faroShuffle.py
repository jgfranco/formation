'''
❓ PROMPT
Legend has it that if a deck of 52 cards is Faro-shuffled 8 times, it will return the original order. A faro shuffle is when a deck is divided in half, and the top half is perfectly interwoven with the bottom half. Write a function to simulate a Faro shuffle. Each card is represented by a 2-3 character string representing the value followed by the suit.

The order of the Faro shuffle must always start with 1 card from the top and then 1 from the bottom. This interweaving repeats until the 2 halves are merged into a single deck again. The tests will call the function 8 times. https://www.youtube.com/shorts/5-7Yfzf3K1E

Just kidding, it's mathematically proven to work. This video provides a mathematical proof and a complete view of the deck after each interweaving: https://www.youtube.com/watch?v=FUDv1QR_N4w&t=1798s

Example(s)
newDeckOrder = [
  'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
  'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
  'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C', 'AC',
  'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AH']

firstFaro = faro(newDeckOrder)
firstFaro == [
  'AS', 'KC', '2S', 'QC', '3S', 'JC', '4S', '10C', '5S', '9C', '6S', '8C', '7S',
  '7C', '8S', '6C', '9S', '5C', '10S', '4C', 'JS', '3C', 'QS', '2C', 'KS', 'AC',
  'AD', 'KH', '2D', 'QH', '3D', 'JH', '4D', '10H', '5D', '9H', '6D', '8H', '7D',
  '7H', '8D', '6H', '9D', '5H', '10D', '4H', 'JD', '3H', 'QD', '2H', 'KD', 'AH']
 

🔎 EXPLORE
List your assumptions & discoveries:

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: create a "first half array" and a "second Half array", use pointers to navigate 
the two in turns  and rewrite the original array
Time: O(n) we traverse once the original array
Space: O(n) we need to store the two halves in two arrays
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function faro(deck) {
def faro(deck: list[str]) -> list[str]:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def faro(deck):
  deckSize = len(deck)
  
  firstHalf = deck[:(deckSize//2)]
  secondHalf = deck[(deckSize//2):]

  a = b = 0
  firstHalfTurn = True
  for i in range(deckSize):                       
    if firstHalfTurn:
      deck[i] = firstHalf[a]
      a +=1
      firstHalfTurn = False
    else:
      deck[i] = secondHalf[b]
      b +=1
      firstHalfTurn = True

  return deck

newDeckOrder = [
  'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
  'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
  'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C', 'AC',
  'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AH']



for i in range(8):
  newDeckOrder = faro(newDeckOrder)
  print(f'iteration: {i+1}')

print(newDeckOrder)

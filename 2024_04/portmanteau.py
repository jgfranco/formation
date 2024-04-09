
'''
Given three words, determine if the third word is potentially a portmanteau of the first two.

A portmanteau (https://en.wikipedia.org/wiki/Portmanteau) is a word that is made by taking the start of one word and the end of another and mashing them together. Brunch is a great example, combining the first 2 letters of "breakfast" with the last 4 of "lunch".

Compound words aren't considered portmanteaus, so "football" is not a portmanteau of "foot" and "ball". At least one of the two words needs to be truncated.
 

EXAMPLE(S)
isPortmanteau("smoke", "fog", "smog") == True (sm + og)
isPortmanteau("snake", "fog", "smog") == False
isPortmanteau("lunch", "breakfast", "brunch") == True (br + unch)
isPortmanteau("shrink", "inflation", "shrinkflation") == True (shrink + flation)
isPortmanteau("foot", "ball", "football") == False
 

 w1    w2            p
 lunck breakfast     brunch

lunch and brunch = 0
breakfast bryunch = 2 


function(w1, w2):
  returns the amount of chars that coincide in the begining

   traverse word that matches and proposed from the end until they dont coincide and count the amount of chars that are the same

  brunch breakfast 2
  brunch lunch 4

  check thhat the sum of the chars that coincided is equal or greater thant the length of the proposed word

FUNCTION SIGNATURE
function isPortmanteau(word1, word2, proposed) {
def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
'''


'''
def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
  def check(w1: str, w2: str):
    p1 = 0
    while p1 < len(w1) and p1 < len(proposed) and proposed[p1] == w1[p1]:
      p1 += 1
    p1 -= 1 # the loop iterated 1 too far
#lunch breakfast brunch
    p2 = len(proposed) - 1
    s2 = len(w2) - 1
    while s2 >= 0 and proposed[p2] == w2[s2]:
      s2 -= 1
      p2 -= 1

    return p1 >= p2 and p2 < len(proposed) - 1

  # Rule out compounds
  if proposed == word1 + word2: return False
  if proposed == word2 + word1: return False

  # The portmanteau can't exactly match either source word
  if proposed == word1 or proposed == word2: return False

  return check(word1, word2) or check(word2, word1)
'''

def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
  if word1 + word2 == proposed or word2 + word1 == proposed: return False
  
  def checkBeginning(word1, word2):
    counter = 0
    for i in range(len(word1)):
      if i < len(word2) and word1[i] == word2[i]:
        counter +=1
      else: break
    return counter

  def checkEnding(word1, word2):
    counter = 0
    pointer = -1


    # lunch brunch
    while abs(pointer) <= len(word1) and abs(pointer) <= len(word2) and word1[pointer] == word2[pointer]:
      counter +=1
      pointer -= 1

      
      
    return counter
      

  word1Counter = checkBeginning(word1, proposed)
  word2Counter = checkBeginning(word2, proposed)

  if word1Counter > word2Counter:
    word2Counter = checkEnding(word2, proposed)
  else:
    word1Counter = checkEnding(word1, proposed)

  return len(proposed) <= word1Counter+ word2Counter
  

print(isPortmanteau("foot", "ball", "football"), "expect False" )
print(isPortmanteau("smoke", "fog", "smog"), "expect True")
print(isPortmanteau("snake", "fog", "smog"), "expect False")
print(isPortmanteau("shrink", "inflation", "shrinkflation"), "expect True")
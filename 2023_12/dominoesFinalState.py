"""/*
'''
You're given an array containing either '.', 'L', or 'R' values. These values represent a starting state of a row of dominoes. L means the domino has been pushed to the left. R means the domino has been pushed to the right. All elements to the left  of an L get pushed to the left and all elements to the right of an R get pushed to the right. If a domino is pushed in both directions simultaneously, it stays up.

Given the starting state array, return the updated array representing the final state of the dominos. All dominos should be L, R or . if it stays standing upright.
 

EXAMPLE(S)
[., L, ., R, .] -> [L, L, ., R, R]
[., R, ., ., L, .] -> [., R, R, L, L, .]
[., R, ., ., ., L, .] -> [., R, R, .,  L, L, .]
[., R, ., L, ., L, ., R, .] -> [., R, ., L, L, L, ., R,R]
 
[., R, ., ., L, L] => [., R, R, L, L, L]
[., R, ., ., L, L] => TEMP [0,7,6,5,0,0]
[., R, ., ., L, L] => TEMP [0,7,1,-1,-7,-7]
[., R, ., ., L, L] => TEMP [0,7,-5,-6,-7,-7]

[., R, ., ., L, L]
    ^  R  L  ^   

Psuedo Code

  create copy of array same length with 0's
  Calculate 'right' forces (iterate 0->n)
    keep a variable R that keeps track of force acting on any given domino
      This R is set to 0 if we encounter any 'L'
      This force is set to n+1 if we encounter any 'R'
      As we continue we decrement R by -1 unless R is equal to 0
      
    if we see a 'L' -> 0
  Calculate 'left' forces (iterate n->0)
    do the opposite where = -n-1 -> +1 if not 0
    if we see a 'R' -> 0
  At the end iterate through if copy[n] < 0: L if copy[n] > 0: R else '.'

[., L, ., R, .] -> [L, L, ., R, R] => 
^
L=4
[-4,-5,0,5,4]
[L, L, ., R, R]


FUNCTION SIGNATURE
def finalDominosState(dominoes: list[str]):
'''

*/

function determineForces(direction, dominoes, ret){
  //for (let domino of dominoes) {
  let force = 0;
  for (let i = 0; i < dominoes.length; i++) {
    let domino = dominoes[i]
    if (domino === direction) {
      if (direction === 'R'){
        force = dominoes.length + 1
      } else{
        force = - dominoes.length - 1
      }
      
    } else if (domino !== direction && domino !== '.') {
      force = 0
    } else if (force !== 0) {
      if (direction === 'R'){
        force -= 1
      } else{
        force += 1
      }
      
    }
    if (direction === "R"){
      ret[i] += force
    }
    else{
      ret[i] += force
    }
  }
  return ret
}


/*
[., L, ., R, .] -> [L, L, ., R, R]
[., R, ., ., L, .] -> [., R, R, L, L, .]
[., R, ., ., ., L, .] -> [., R, R, .,  L, L, .]
[., R, ., L, ., L, ., R, .] -> [., R, ., L, L, L, ., R,R]
*/
//console.log(['.', 'L', '.', 'R', '.'])
console.log(finalDominosState(['.', 'L', '.', 'R', '.']))
console.log(finalDominosState(['.', 'R', '.', '.', 'L', '.']))
console.log(finalDominosState(['.', 'R', '.', '.', '.', 'L', '.']))
console.log(finalDominosState(['.', 'R', '.', 'L', '.', 'L', '.', 'R', '.'] ))
"""

def determineForces(direction, dominoes, forces):
  force = 0
  for i in range(len(dominoes)):
    domino = dominoes[i]
    if domino == direction:
      force = len(dominoes) + 1
    elif domino != direction and domino != '.': 
      force = 0
    elif force != 0:
      force -=1

    forces[i] += force if direction == "R" else -force
  
  return forces


def finalDominosState(dominoes):
  state = [0] * len(dominoes)

  state = determineForces("R", dominoes, state)
  print(state)
  state = determineForces("L", dominoes[::-1], state[::-1])
  
  state.reverse()
  print(state)

  for i in range(len(state)):
    if (state[i] > 0):
      state[i] = 'R'
    elif (state[i] < 0):
      state[i] = 'L'
    else:
      state[i] = '.'
  return state



"""print(finalDominosState(['.', 'L','.','R','.']))
print(finalDominosState(['.', 'R', '.', '.', 'L', '.']))
                        #  l    r      
print((finalDominosState(['.', 'R', '.', 'L', '.', 'L', '.', 'R', '.'] )))"""


def finalDominoesStateAlt(dominoes):
  pass

  left = 0
  right =0

  def fillGap(left, right):
    while left < right:
      dominoes[left] = "R"
      dominoes[right] = "L"
      left +=1
      right -=1

  while right < len(dominoes):
    if dominoes[right] == ".":
      if dominoes[left]== "R" and right == len(dominoes)-1:
        while left <= right:
          dominoes[left] = "R"
          left +=1
      right +=1
    elif dominoes[right] == "L":
      if dominoes[left] == ".":
        while left < right:
          dominoes[left] = "L"
          left +=1
        right +=1
      elif dominoes[left] == "R":
        fillGap(left, right)
        left = right
        right += 1
      elif dominoes[left] == "L":
        while left <= right:
          dominoes[left] = "L"
          left +=1
        right +=1
    elif dominoes[right] == "R":
      left = right
      right += 1
    
  return dominoes

#                            lr
print(finalDominoesStateAlt(['.', 'L','.','R','.']))
print(finalDominoesStateAlt(['.', 'R','.','L','.']))
print(finalDominoesStateAlt(['.', 'R', '.', '.', 'L', '.']))
#                                            l          r
print(finalDominoesStateAlt(['.', 'R', '.', 'L', '.', 'L', '.', 'R', '.'] ))
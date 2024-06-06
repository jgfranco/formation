"""
Given a chess board with a set of bishops, return the number of pairs of bishops that are attacking each other. Bishops will be given as an array of tuples.
 

EXAMPLE(S)
Bishops: [(0, 0), (2, 2), (1, 2), (3, 0)]
This would look like this:

x . . . .
. . x . .
. . x . .
x . . . .
. . . . .

In this case, there are 2 pairs of bishops attacking each other.

- attacking = within the dia
- don't worry about empty array edgecase

 

FUNCTION SIGNATURE

*/
const bishops = [[0, 0], [2, 2], [1, 2], [3, 0]]

function pairsOfAttackingBishops(bishops) {
  const columns = {}
  const downColumns = {}
  let pairs = 0;

  for (const [i, j] of bishops) {
    const upCol = i + j; // 4
    const downCol = i - j; // 0

    columns[upCol] = columns[upCol] + 1 || 0;
    pairs = pairs + columns[upCol];

    downColumns[downCol] = downColumns[downCol] + 1 || 0;
    pairs = pairs + downColumns[downCol];
  }

  return pairs;

}

console.log(pairsOfAttackingBishops(bishops))
"""


def pairsOfAttackingBishops(bishops):

  descending = {}
  ascending = {}
  count  = 0
  for x,y in bishops:
    minus = x - y 
    plus = x + y
    descending[minus] = descending.get(minus, -1) + 1
    ascending[plus] = ascending.get(plus, -1) + 1

    
    count += ascending[plus] + descending[minus]
    

  return count

bishops= [(0, 0), (2, 2), (1, 2), (3, 0)]
print(pairsOfAttackingBishops(bishops))


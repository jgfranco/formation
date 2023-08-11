'''
Generate all plus & minus expressions that equals target

Given a string that contains only digits from 0 to 9, and an integer value, *target*. Print all expressions which evaluate to *target* using the plus(+) and minus(-) binary operators between the digits.

You will likely need a helper function to recurse. You can use a loop within your recursive function because we're not monsters.
 

EXAMPLE(S)
generateExprs("123", 6) == ['1 + 2 + 3']
generateExprs("125", 7) == ['12 - 5']
generateExprs("420", 420) == ['420']
generateExprs("1210", 2) == ['1 + 2 - 1 + 0','1 + 2 - 1 - 0','12 - 10']
 

FUNCTION SIGNATURE
function generateExprs(seq, target) {
def generateExprs(seq: str, target: int) -> None:
'''


def generateExprs(seq: str, target: int) -> None:
  results = []

  def calculateExpr(curExpr: str, seq: str, target: int, curIdx: int, total: int) -> None:
    # Base case is at the end index of the sequence and the total matches target
    # print(f'curExpr: {curExpr}, seq: {seq}, target: {target}, curIdx: {curIdx}, total: {total}')
    if curIdx == len(seq) and total == target:
      results.append("".join(curExpr))
      return

    # loop to put operator at all positions
    for i in range(curIdx, len(seq)):
      # ignore numbers with a leading 0
      if seq[curIdx] == '0' and i != curIdx:
        break

      # grab 1+ chars for processing
      segment = seq[curIdx: i + 1]
      segmentVal = int(segment)

      # a binary operator needs 2 operands and this is
      # the first index so simply send the segment's segmentVal
      if curIdx == 0:
        calculateExpr(curExpr + segment, seq, target, i + 1, segmentVal)
      else: # try (+) and (-) each time
        calculateExpr(curExpr + "+" + segment, seq, target, i + 1, total + segmentVal)
        calculateExpr(curExpr + "-" + segment, seq, target, i + 1, total - segmentVal)

  calculateExpr(curExpr="", seq=seq, target=target, curIdx=0, total=0)
  return results


print(set(generateExprs("123", 6)) == {'1+2+3'}) # plus only
print(set(generateExprs("125", 7)) == {'12-5'}) # minus only
print(set(generateExprs("1236", 0)) == {'1+2+3-6'}) # mix
print(set(generateExprs("1235", -3)) == {'1-2+3-5'}) # mix
print(set(generateExprs("12036", 0)) == {'1+2+0+3-6', '1+2-0+3-6'})
print(set(generateExprs("12036", 18)) == {'1+20+3-6'})
print(set(generateExprs("1010", 9)) == {'10-1+0', '10-1-0'})
print(set(generateExprs("420", 420)) == {'420'})
print(set(generateExprs("1210", 2)) == {'12-10', '1+2-1+0', '1+2-1-0'})
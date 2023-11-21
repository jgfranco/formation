
'''
Write a program that checks whether an integer is a palindrome.
 

EXAMPLE(S)
isPalindrome(535) == true
isPalindrome(77) == true
isPalindrome(15) == false
 

FUNCTION SIGNATURE
func isPalindrome(input: Int) -> Bool
'''

'''
Explore
A single digit is a palindrome
Assume that the input will always be an integer

Brainstorm
Silly approach:
 turn input into a string
 split chars
 reverse and join
 compare against input
Another approach:
 generate a new integer by:
  taking input % 10 repeatedly
  update input Math.floor(input / 10)
  until input === 0
  compare generated integer again original input

Plan
create a temporary variable = input
create a new integer = 0
while tmp > 0:
  new integer *= 10
  new integer += tmp % 10

return new integer === input

Implement

Verify

*/

const isPalindrome = input => {
  if (input < 0) return false;
  
  let tmp = input;
  let curr = 0;

  while (tmp > 0) {
    curr *= 10;
    curr += tmp % 10;
    tmp = Math.floor(tmp / 10);
  }

  return curr === input;
}
console.log(isPalindrome(535) == true);
console.log(isPalindrome(77) == true);
console.log(isPalindrome(15) == false);
console.log(isPalindrome(-515) == false);
'''

def isPalindrome(number):

  reversed = 0
  copy = number

  while copy >0:
    reversed *= 10
    reversed += copy %10
    copy //= 10

  return reversed == number

print(isPalindrome(414))
print(isPalindrome(44))
print(isPalindrome(4))
print(isPalindrome(124))
print(isPalindrome(32))
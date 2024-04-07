'''
You're working on the UI for the text messaging app for a phone. In a message notification, there is limited space, so the entire message cannot be shown, so the app designer wants to show a truncated form of the message in the space allotted.

The message will be words separated by spaces. Don't worry about punctuation or other special characters. Consider any series of characters other than spaces as a word.

Given an input text message (string) and a maximum number of characters (integer), return the truncated string.

The rules for truncation are as follows:
- If the string must be truncated, it must be indicated as such with a trailing '...', a space then three periods.
- If there is a word before the '...' then there must also be a space.
- Including the truncation indicator, the resulting string must be less than the provided maximum number of characters.
- Truncation can only happen on word boundaries (mustn't include partial words)
- If the whole string fits in the allotted space, no truncation is necessary.
 

EXAMPLE(S)
truncateMessage("This is a test message", 8) == 'This ...'
truncateMessage("This is a test message", 11) == 'This is ...'
truncateMessage("This is a test message", 15) == 'This is a ...'
truncateMessage("This is a test message", 20) == 'This is a test ...'
truncateMessage("This is a test message", 25) == 'This is a test message'
 

FUNCTION SIGNATURE
function truncateMessage(message, threshold) {
def truncateMessage(message: str, threshold: int) -> str:
'''


def truncateMessage(message, threshold):
  if len(message) <= threshold:
    return message

  words = message.split('')
  truncatedMessage = ""
  for word in words:
    if len(word) + 4 <= threshold:
      truncatedMessage += word + " "
      threshold -= len(word) + 1
    else:
      truncatedMessage += "..."
      break
  return truncatedMessage

  
print(truncateMessage("", 3) == '')
print(truncateMessage("ab", 3) == 'ab')
print(truncateMessage("abc", 3) == 'abc')
print(truncateMessage("abc", 4) == 'abc')
print(truncateMessage("abcd", 4) == 'abcd')
print(truncateMessage("abcd", 3) == '...')
print(truncateMessage("Hello", 4) == '...')
print(truncateMessage("Hello", 5) == 'Hello')
print(truncateMessage("Hello Cat", 8) == '...')
print(truncateMessage("Hello Cat", 9) == 'Hello Cat')
print(truncateMessage("Hello Cat", 5) == '...')
print(truncateMessage("Hello Rufus", 9) == 'Hello ...')
print(truncateMessage("Hello Rufus", 11) == 'Hello Rufus')
print(truncateMessage("Hello Rufus", 12) == 'Hello Rufus')

print(truncateMessage("This is a test message", 3) == '...')
print(truncateMessage("This is a test message", 7) == '...')
print(truncateMessage("This is a test message", 8) == 'This ...')
print(truncateMessage("This is a test message", 10) == 'This ...')
print(truncateMessage("This is a test message", 11) == 'This is ...')
print(truncateMessage("This is a test message", 15) == 'This is a ...')
print(truncateMessage("This is a test message", 20) == 'This is a test ...')
print(truncateMessage("This is a test message", 25) == 'This is a test message')
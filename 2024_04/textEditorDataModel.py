'''
We're going to build the data model for a text editor that supports the basic operations needed for typing. This data model will take the form of a class that has methods for:
- typing one character at a time
- backspace and delete to remove text one character at a time
- moving the cursor

How can this class be designed so that the main operations are as efficient as possible?
 

EXAMPLE(S)
const editor = new TextEditor("Text").moveEnd();
console.log(editor.toString(), "Text");
editor.backspace();
console.log(editor.toString(), "Tex");
editor.addChar('t'). addChar(" ").addChar("E").addChar("d").addChar("i").addChar("t");
console.log(editor.toString(), "Text Edit");
editor.moveStart().delete().delete().delete().delete().delete();
console.log(editor.toString(), "Edit");

const e2 = new TextEditor("otter");
console.log(e2.toString(), "otter");
e2.backspace().backspace().backspace().backspace().backspace();
console.log(e2.toString() === "", true);
e2.addChar("a").moveBack().delete();
console.log(e2.toString() === "", true);

'''

class Node:
  def __init__(self, value, prev = None, next = None) -> None:
    self.value = value
    self.prev = prev
    self.next = next

class TextEditor:     
  # initialize the editor, optionally with some starter text
  def __init__(self, initialText) -> None:
    self.headSentinel = Node("head")
    self.tailSentinel = Node("tail")
    self.cursor = self.headSentinel

    for char in initialText:
      newNode = Node(char)
      newNode.prev = self.cursor
      self.cursor.next = newNode
      self.cursor = self.cursor.next

    if not self.headSentinel.next:
      self.headSentinel.next = self.tailSentinel

    self.cursor.next = self.tailSentinel
    self.tailSentinel.prev = self.cursor
    # print(self.cursor.value)
    # print(self.headSentinel.next.value)
    # print(self.tailSentinel.prev.value)


  # remove the character before the cursor
  def backspace(self):
    pass

  # remove the character at the cursor. Cursor moves to the
  # next character.
  def delete(self):
    if self.cursor != self.headSentinel and self.cursor != self.tailSentinel:
      self.cursor = self.cursor.prev
      self.cursor.next = self.cursor.next.next
      self.cursor.next.prev = self.cursor
      self.cursor = self.cursor.next

  
  # add a new character before the cursor
  def addChar(self, char):
  
    
    
  # move the cursor back one
  def moveBack(self):
    pass

  #  move the cursor forward one
  def moveNext(self):
    if  self.cursor.next.next:
      self.cursor = self.cursor.next
  
  # Move the cursor to the start. A new
  # character added here will be the first.
  def moveStart(self):
    pass

  # move the cursor to the end. A new
  # character here will be last.
  def moveEnd(self):
    pass


  # Return the text currently in the editor as a single string.
  # Can be O(n) in the size of the current text.
  def __str__(self):
    current = self.headSentinel.next
    result = []
    while current and current.value != "tail":
      result.append(current.value)
      current = current.next

    return "".join(result)

  

TE = TextEditor("Hello")
TE.delete()
print(TE.cursor.value)



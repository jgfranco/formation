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


Approach: Array
delete/insertion at any random position : O(n)
add: O(n)

Approach: Doubly Linked List
backspace/delete: O(1)
add: O(1)
'''
class Node:
  def __init__(self, value, prev = None, next = None):
    self.value = value
    self.prev = prev
    self.next = next


class TextEditor:
  # initialize the editor, optionally with some starter text
  def __init__(self, initialText = ""):
    self.head = None
    self.tail = None
    self.cursorNode = None
    if len(initialText) > 0:
      for char in initialText:
        self.addChar(char)
  

  
  # remove the character before the cursor 
  def backspace(self):
     if self.moveBack():
       self.delete()
  
  # remove the character at the cursor
  def delete(self):
    if self.cursorNode:
      if self.cursorNode.prev and self.cursorNode.next: #happy case, we have a letter behind and a letter going forward
        self.cursorNode.prev.next = self.cursorNode.next
        self.cursorNode.next.prev = self.cursorNode.prev
        self.moveNext()
      elif not self.cursorNode.prev and not self.cursorNode.next: # there's only one character in the string 
        self.cursorNode = None
        self.head = None
        self.tail = None
      elif not self.cursorNode.prev: # theres no previous node, head needs to be modified
        self.moveNext()
        self.cursorNode.prev = None
        self.head = self.cursorNode
      elif not self.cursorNode.next: # theres no next node, tail needs to be modified
        self.moveBack()
        self.cursorNode.next = None
        self.tail = self.cursorNode      
    else:
      print("nothing there to delete")


  def addChar(self, char):
    if self.cursorNode and not self.cursorNode.next:
      self.cursorNode.next = Node(char)
      self.cursorNode.next.prev = self.cursorNode
      self.cursorNode = self.cursorNode.next
      self.tail = self.cursorNode
    elif self.cursorNode:
      next = self.cursorNode.next
      newNode = Node(char)
      self.cursorNode.next = newNode
      newNode.next = next
      newNode.prev = self.cursorNode
      next.prev = newNode
      self.cursorNode = self.cursorNode.next
    else:
      self.cursorNode = Node(char)
      self.head = self.cursorNode
      self.tail = self.cursorNode
    
  

  # move the cursor back one
  def moveBack(self):  # can work in constant time
    if self.cursorNode.prev:
      self.cursorNode = self.cursorNode.prev
      return True
    return False

  # move the cursor forward one
  def moveNext(self): # can work in constant time
    if self.cursorNode.next:
      self.cursorNode = self.cursorNode.next
  

  # Move the cursor to the start. A new
  # character added here will be the first.
  def moveStart(self): 
    self.cursorNode = self.head

  def printCharAtCursor(self):
    print(f'current char: {self.cursorNode.value}')

  # move the cursor to the end. A new
  # character here will be last.
  def moveEnd(self):
    self.cursorNode = self.tail

  # Return the text currently in the editor as a single string.
  # Can be O(n) in the size of the current text.
  def __str__(self):
    result = ""
    cursor = self.head
    while(cursor):
      result += cursor.value
      cursor = cursor.next
    return result
  
TE = TextEditor("Helo")
TE.printCharAtCursor()
TE.moveBack()
TE.printCharAtCursor()
TE.addChar("p")
print(TE)
  


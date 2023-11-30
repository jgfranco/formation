"""138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list."""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        def getRandomIndex(randomNode):
            curr = head
            index = 0
            while curr:
                if curr == randomNode:
                    return index
                curr = curr.next
                index +=1
            return -1

        def getRandomNode(newListHead, randomIndex):
            if randomIndex ==0: return newListHead
            randomNode = Node(-1)
            randomNode.next = newListHead
            while randomNode and randomIndex >= 0:
                randomNode = randomNode.next
                randomIndex -=1
            return randomNode
            
        original = head
        newList = Node(-1)
        newListHead = newList

        randomIndices = []

        while original:
            newList.next = Node(original.val)
            if original.random:
                randomIndices.append(getRandomIndex(original.random))
            else:
                randomIndices.append(-1)
            original = original.next
            newList = newList.next
        
        newList = newListHead.next

        p = 0
        while newList:
            if randomIndices[p] == -1:
                newList.random = None
            else:
                newList.random = getRandomNode(newListHead.next, randomIndices[p])
            p +=1
            newList = newList.next
        return newListHead.next



            
        
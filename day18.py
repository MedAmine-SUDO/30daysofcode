import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.__stak = []
        self.__queue = []

    def pushCharacter(self, ch):
        """Pushes Charachter onto a stack."""
        self.__stak.append(ch)

    def enqueueCharacter(self, ch):
        """Enqueues a character in the queue."""
        self.__queue.append(ch)

    def popCharacter(self):
        """Pops and return the character at the top of the stack."""
        if len(self.__stak) > 0:
            return self.__stak.pop()
        else:
            print("Stack is empty.")
            return False    

    def dequeueCharacter(self):
        """Dequeues and returns the first characters in the queue."""
        if len(self.__queue) > 0:
            return self.__queue.pop(0)
        else:
            print("Queue is empty.")
            return False


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
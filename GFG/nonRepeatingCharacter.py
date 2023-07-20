from collections import deque
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        dict = {}
        queue = deque()
        res = ""
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
            
            queue.append(char)
            
            while queue and dict[queue[0]] > 1:
                queue.popleft()
        if queue:
            return queue[0]
        else:
            return -1

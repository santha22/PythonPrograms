class Solution:
    

    def longestChain(self, n, words):
        # Code here 
        # sort the string in ascending order of length of string
        words.sort(key=len)
        word_dict = {}
        maxi = 1
        
        for word in words:
            if len(word) == 1:
                word_dict[word] = 1
                
            else:
                word_dict[word] = 1
                for i in range(len(word)):
                    predecessor = word[:i] + word[i + 1:]
                    if predecessor in word_dict:
                        word_dict[word] = max(word_dict[word], 1 + word_dict[predecessor])
                        
            maxi = max(maxi, word_dict[word])
            
        return maxi

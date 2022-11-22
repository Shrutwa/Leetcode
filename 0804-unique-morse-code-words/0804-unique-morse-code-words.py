from string import ascii_lowercase
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict1 = {}
        l1 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        char = []
        code = ''
        codes = set()
        
        for i,c in enumerate(ascii_lowercase):
            
            dict1[chr(ord(c))]=l1[i]
        
        for s in range(len(words)):
            char = list(words[s])
            for c in char :
                code+=dict1[c]
            codes.add(code)
            code = ''   
            
        return len(codes)
        
        
                
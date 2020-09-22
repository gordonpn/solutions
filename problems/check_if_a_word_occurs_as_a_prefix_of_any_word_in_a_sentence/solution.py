class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split(" ")
        
        for index, value in enumerate(sentence_list):
            if value.startswith(searchWord):
                return index + 1
        
        return -1
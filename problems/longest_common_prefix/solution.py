class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common_prefix = strs[0]
        
        for strs_i in range(1, len(strs)):
            if not common_prefix:
                return ""
            current_prefix = ""
            
            for i, c in enumerate(strs[strs_i]):
                if i + 1 > len(common_prefix) or c != common_prefix[i]:
                    break
                    
                current_prefix = current_prefix + c
                    
            common_prefix = current_prefix
                    

        
        return common_prefix

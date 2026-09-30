class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # left , right =  0, 0 
        # ans = [[]]
        # sort_string = sorted(strs)
        # for left in range (0, len(strs) - 1):
        #     for right in range (left + 1 , len(strs)):
        #         if strs[left] == strs[right]:
                    
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the characters to create a unique key for anagrams
            # e.g., "eat" -> "aet", "tea" -> "aet"
            sorted_word = "".join(sorted(word))
            
            # Append the original word to its sorted key group
            anagram_map[sorted_word].append(word)
            
        # Return all the grouped anagram list values
        return list(anagram_map.values())
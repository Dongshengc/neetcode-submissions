class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
            
        left = 0
        right = 1
        substring = s[0]
        max_length = 1

        while right < len(s):

            if s[right] not in substring:
                # print(s[right])
                substring += s[right]
                right += 1
            else:
                left = substring.find(s[right])
                substring = substring[left+1:]
                substring += s[right]
                right += 1

            max_length = max(max_length, len(substring))
            # print(max_length)
        
        return max_length
                

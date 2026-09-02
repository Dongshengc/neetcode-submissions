class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        left = 0
        substring = set()
        max_length = 0

        for i in range(len(s)):


            while s[i] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[i])


            max_length = max(max_length, i - left + 1)
            # print(max_length)
        
        return max_length

                

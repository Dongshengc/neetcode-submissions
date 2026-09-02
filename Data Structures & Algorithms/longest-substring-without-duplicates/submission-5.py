class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        left = 0
        right = 1
        substring = set(s[0])
        max_length = 1

        while right < len(s):

            if s[right] not in substring:
                # print(s[right])
                substring.add(s[right])
                right += 1
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                # pos = substring.find(s[right]) + 1
                # substring = substring[pos:]
                    left += 1
                substring.add(s[right])
                right += 1

            max_length = max(max_length, right - left)
            # print(max_length)
        
        return max_length

                

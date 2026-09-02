class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
        
    #     if not s:
    #         return 0

    #     left = 0
    #     right = 1
    #     substring = s[0]
    #     max_length = 1

    #     while right < len(s):

    #         if s[right] not in substring:
    #             # print(s[right])
    #             substring += s[right]
    #             right += 1
    #         else:
    #             pos = substring.find(s[right]) + 1
    #             substring = substring[pos:]
    #             left += pos
    #             substring += s[right]
    #             right += 1

    #         max_length = max(max_length, right - left)
    #         # print(max_length)
        
    #     return max_length
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                

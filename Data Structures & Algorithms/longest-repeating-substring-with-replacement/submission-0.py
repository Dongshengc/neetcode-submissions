class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = {}
        max_freq = 0
        max_length = 0
        left = 0

        for right in range(len(s)):

            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1

            max_freq = max(max_freq, max(hashmap.values()))

            if right - left + 1 - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left +1)

        return max_length



class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        push_list = ["(", "{", "["]
        pop_list = [")", "}", "]"]
        pair_map = {"(": ")", "{": "}", "[":"]"}
        for char in s:

            if char in push_list:
                stack.appendleft(char)
            elif char in pop_list:
                if stack:
                    return_char = stack.popleft()
                    if pair_map[return_char] != char:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False
class Solution:
    def hammingWeight(self, n: int) -> int:

        power = 31 
        cnt = 0 

        while power:

            base = 2 ** power

            if n // base == 1:
                cnt += 1
            
            n = n % base 

            if n == 0:
                return cnt 
                
            power -= 1

        return cnt + 1
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == 1:
            return -(-piles[0] // h)

        k_min = 1
        k_max = max(piles)
        max_pile = max(piles)

        while k_min <= k_max:
            k_mid = (k_min + k_max) // 2
            print(k_mid)
            h_mid = 0
            for pile in piles:
                h_mid += -(-pile // k_mid)
            
            if h_mid > h:
                k_min = k_mid + 1
            elif h_mid < h:
                k_max = k_mid - 1
            else:
                if max_pile // (k_mid - 1) > max_pile // k_mid:
                    return k_mid
                else:
                    k_max = k_mid - 1
            print("range", k_min, k_max)

        if h_mid > h:
            return k_mid + 1
        else:
            return k_mid
 
        
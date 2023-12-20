class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        n = len(prices)
        min1 = min2 = float("inf")

        for p in prices:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p

        minleftover = money - min1 - min2 

        return minleftover if minleftover >= 0 else money

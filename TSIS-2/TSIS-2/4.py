class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        b = 0
        a = b
        for i in gain:
            b +=i
            if a > b:
                a=b
        return b
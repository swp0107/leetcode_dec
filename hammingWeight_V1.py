class Solution:
    def hammingWeight(self, n: int) -> int:
        x = list(format(n, 'b'))
        length = len(x)-1
        count = 0
        while (length >= 0):
            if x[length] == '1':
                count += 1
            length -= 1
        return (count)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = list(format(x, 'b'))
        y = list(format(y, 'b'))
        if len(x) > len(y):
            dif = len(x) - len(y)
            while (dif > 0):
                y.insert(0, '0')
                dif -= 1
        elif (len(y) > len(x)):
            dif = len(y) - len(x)
            while (dif > 0):
                x.insert(0, '0')
                dif -= 1
        length = len(x)-1
        count = 0
        while (length >= 0):
            if x[length] != y[length]:
                count += 1
            length -= 1
        return (count)

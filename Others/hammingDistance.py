class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        try:
            xCon = bin(x).replace("0b", "").zfill(1)
            yCon = bin(y).replace("0b", "").zfill(1)

            i = 2
            while len(xCon) > len(yCon):
                yCon = yCon.zfill(i)
                i += 1

            j = 2
            while len(xCon) < len(yCon):
                xCon = xCon.zfill(j)
                j += 1

            counter = 0
            for index, value in enumerate(xCon):
                if xCon[index] != yCon[index]:
                    counter += 1

            return(counter)
        except:
            return (None)

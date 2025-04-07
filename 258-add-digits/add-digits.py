class Solution:
    def addDigits(self, num: int) -> int:
        
        while len(str(num)) > 1:
            snum = str(num)
            total = 0
            for i in snum:
                total = total + int(i)
            num = total
        return num
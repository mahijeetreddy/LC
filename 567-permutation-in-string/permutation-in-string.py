class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        winlen = len(s1) #2 in this case
        left = 0
        right = left + winlen
        for i in range(len(s2)):
            window = s2[left:right]
            count2 = Counter(window)
            if count1 == count2:
                return True
            left +=1
            right +=1
        return False


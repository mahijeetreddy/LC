import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        al = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return al == al[::-1]

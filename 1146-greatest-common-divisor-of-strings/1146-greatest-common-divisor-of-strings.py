class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def div(x, y):
            while y:
                x, y = y, x % y
            return x
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:div(len(str1), len(str2))]
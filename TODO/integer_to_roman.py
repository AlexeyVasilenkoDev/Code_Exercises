link = "https://leetcode.com/problems/integer-to-roman/"


class Solution:
    result = ''

    def intToRoman(self, num: int) -> str:
        dictionary = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        while num > 0:
            for letter, digit in list(reversed(list(dictionary.items()))):
                if num / digit >= 1:
                    self.result += letter
                    num = num - digit
                    return self.intToRoman(num)
        return self.result


print(Solution().intToRoman(1994))

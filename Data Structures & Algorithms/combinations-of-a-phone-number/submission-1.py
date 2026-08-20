class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res, sol = [], []

        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = {
            "2": "abc",
            "3": "def",
            "4" : "ghi",
            "5": "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(i):
            if i == len(digits):
                res.append(''.join(sol))
                return

            possible_chars = alpha_dict[digits[i]]

            for c in range(len(possible_chars)):
                char = possible_chars[c]

                sol.append(char)
                backtrack(i+1)
                sol.pop()

        backtrack(0)

        return res

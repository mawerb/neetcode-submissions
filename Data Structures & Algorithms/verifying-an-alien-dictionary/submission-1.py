class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha_order = dict()
        
        for i in range(len(order)):
            alpha_order[order[i]] = i

        for i in range(len(words) - 1):
            for char in range(len(words[i])):
                if char == len(words[i+1]):
                    return False
                elif alpha_order[words[i][char]] > alpha_order[words[i+1][char]]:
                    return False
                elif alpha_order[words[i][char]] < alpha_order[words[i+1][char]]:
                    break
        
        return True

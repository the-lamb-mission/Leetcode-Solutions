from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numHash = {
            "2":["a", "b", "c"], 
            "3":["d", "e", "f"], 
            "4":["g", "h", "i"], 
            "5":["j", "k", "l"], 
            "6":["m", "n", "o"], 
            "7":["p", "q", "r", "s"], 
            "8":["t", "u", "v"], 
            "9":["w", "x", "y", "z"], 
        }

        finalComb = numHash[digits[0]]

        for i in range(1, len(digits)):
            finalComb = product(finalComb, numHash[digits[i]])
            finalComb = list(map(lambda a: "".join(a), finalComb))
        
        return finalComb

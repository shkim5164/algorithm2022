from itertools import permutations, product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0:
            return []
        phone_nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        items = []
        for digit in digits:
            items.append(phone_nums[digit])
        product_list = [ "".join(item) for item in list(product(*items))]
        return product_list
        
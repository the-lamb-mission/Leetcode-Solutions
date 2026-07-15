class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        car = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i], car = (digits[i] + car)%10, (digits[i] + car)//10
        if car:
            digits.insert(0, car)
        return digits

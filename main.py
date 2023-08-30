class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        prev = nums[-1]; total = 0
        for i in reversed(nums[:len(nums)]):
            count = 1
            if i > prev: count = -(-i // prev); total += count - 1
            prev = i // count
        return total


test = Solution()
testArr = [3,9,3]
print(test.minimumReplacement(testArr))

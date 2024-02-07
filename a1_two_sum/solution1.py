from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in hashtable:
                return [hashtable[remainder], index]
            hashtable[value] = index
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # o(n)
        # for i in range(len(nums)):
        #     # o(n)
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target and i!=j:
        #             # Time Comp overall O(n**2)
        #             # space = O(1)
        #             return [i, j]
        # return []

        hashMap = {}

        for i, value in enumerate(nums):
            diff = target -  nums[i]
            if diff in hashMap:
                return [hashMap[diff], i] 
            hashMap[value] = i

        
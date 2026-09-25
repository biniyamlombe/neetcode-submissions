class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] +=1
        arr = []

        for key, value in my_dict.items():
            arr.append([value, key])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        

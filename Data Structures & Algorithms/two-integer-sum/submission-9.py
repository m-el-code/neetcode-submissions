class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res = []
        # for i in range(len(nums)-1):  
        #     for j in range(1, len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return list([i, j])

        

        diff = {}

        for x in range(len(nums)):
            test = target - nums[x]
            if test in diff:
                return [diff[test], x]
            else:
                diff[nums[x]] = x
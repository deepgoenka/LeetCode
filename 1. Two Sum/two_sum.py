class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """ Brute Force method - O(N²) """
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return ([i, j])


        """ Optimal Solution - Using HashMap - O(N) """
        Hmap = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in Hmap:
                return [Hmap[diff], ind]
            Hmap[num] = ind

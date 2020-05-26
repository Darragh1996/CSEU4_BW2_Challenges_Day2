class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # dictionary used to store the index of where the numbers counterpart is
        sum_pairs = {}

        for i in range(0, len(nums)):
            # if nums[i] is already in sum_pairs then the other num needed to add to target has already been found
            if nums[i] in sum_pairs:
                index_pair = sum_pairs[nums[i]]
                return [index_pair, i]
            # otherwise store its index under the needed number in the hopes of finding it later
            else:
                counter_part = target - nums[i]
                sum_pairs[counter_part] = i
        # if this point is reached then there is no pairs that add to the target
        return f"no pairs add to target: {target}"


# tests
test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0;
        ans = [0] * ((len(nums) * 2));
        while index < len(nums):
            ans[index] = nums[index];
            ans[index + len(nums)] = nums[index];
            index+=1;
        # In Python, this can be simplified using `return nums + nums'
        return ans;

nums = [1, 3, 4, 2]
test = Solution()
new_array = test.getConcatenation(nums)
print(new_array)

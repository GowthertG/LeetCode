class Solution(object):
    def RemoveDupluicates(self, nums):
        k = 0;
        i = 0;
        while i < len(nums):
            if (i == len(nums) - 1 or nums[i] != nums[i + 1]):
                nums[k] = nums[i];
                k+=1;
            i+=1;
        return (k);
a = Solution();
array = [1, 1, 2];
print(a.RemoveDupluicates(array));

class Solution(object):
    def removeElement(self, nums, val):
        k = 0;
        i = 0;
        while i < len(nums):
            if (nums[i] != val):
                nums[k] = nums[i];
                k+=1;
            i+=1;
        return k;

a = Solution();
nums = [1, 1, 2, 3, 1, 7, 8 ,1, 2, 2];
print(a.removeElement(nums, 1));

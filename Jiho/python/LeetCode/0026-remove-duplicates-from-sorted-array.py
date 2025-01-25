class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # target = n
        target = -101
        remove_nums = []

        # 1, 2, 3, 3, 4
        for i in range(len(nums)):
            if nums[i] == target:
                remove_nums.append(i) # 중복 원소 index 저장
            else: 
                target = nums[i]
        
        # 뒤 index부터 삭제
        for j in range(-1, -1-len(remove_nums), -1):
            nums.pop(remove_nums[j])

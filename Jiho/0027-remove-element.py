class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # remove all occurrences of val in nums in-place
        flag = True
        while flag:
            try: 
                nums.remove(val)
            except:
                flag = False
                
        k = len(nums)
        return k

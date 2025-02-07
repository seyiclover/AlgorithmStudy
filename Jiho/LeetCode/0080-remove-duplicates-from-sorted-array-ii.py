class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # {element: [count, [index]]}
        cnt = {n:[0, []] for n in nums}

        # 삭제해야 하는 idx
        del_idx = []
        
        for i in range(len(nums)):

            idx = i
            element = nums[i]

            cnt[element][0] += 1
            cnt[element][1].append(idx)
            
            # 등장 횟수 2 초과하는 idx 기록
            if len(cnt[element][1])>2:
                del_idx.append(idx)

        # idx 뒤 원소부터 삭제
        del_idx.sort(reverse=True)

        for j in del_idx:
            nums.pop(j)

        k = len(nums)
        return k
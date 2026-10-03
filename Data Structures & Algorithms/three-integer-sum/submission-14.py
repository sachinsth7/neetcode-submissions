class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        if nums[0] > 0:
            return result
        n = len(nums)
        i = 0

        while i < n-2:
            if i >0 and nums[i] == nums[i-1]:
                i +=1
                continue
            j = i+1
            k = n -1 
            target = -nums[i]

            while j<k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j +=1
                    while j < k and nums[k] == nums[k+1]:
                        k -=1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        return result
        
        
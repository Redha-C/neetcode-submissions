class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum_ = nums[i] + nums[j]

                if sum_ == target:
                    return [i, j]

            #two_sum.append((i, sum_))

            #if sum_ == target:
            #    return two_sum.append(i, i+1)

        #return two_sum
            

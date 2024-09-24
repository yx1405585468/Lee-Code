from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ > target:
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        if {nums[i], nums[j], nums[left], nums[right]} not in [set(x) for x in result]:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                        # 跳过相同的元素以避免重复
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        while right > left and nums[left] == nums[left + 1]:
                            left += 1

                        right -= 1
                        left += 1

        return result


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2]

    test = Solution()
    print(test.fourSum(nums=nums, target=8))

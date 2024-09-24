from cgitb import reset
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result

            # 跳过相同的元素以避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]  #
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    # if {nums[i], nums[left], nums[right]} not in [set(x) for x in result]:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1
        return result
    # 超时了
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == nums[j - 1] and nums[j] != nums[i]:
    #                 continue
    #             for k in range(j + 1, len(nums)):
    #                 if nums[k] < 0:
    #                     continue
    #                 if nums[k] == nums[k - 1] and nums[j] != nums[k]:
    #                     continue
    #
    #                 if -nums[k] == nums[i] + nums[j] and {nums[i], nums[j], nums[k]} not in [set(x) for x in
    #                                                                                          result]:
    #                     result.append([nums[i], nums[j], nums[k]])
    #
    #     return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [5, -9, -11, 9, 9, -4, 14, 10, -11, 1, -13, 11, 10, 14, -3, -3, -4, 6, -15, 6, 6, -13, 7, -11, -15, 10, -8,
            13, -14, -12, 12, 6, -6, 8, 0, 10, -11, -8, -2, -6, 8, 0, 12, 3, -9, -6, 8, 3, -15, 0, -6, -1, 3, 9, -5, -5,
            4, 2, -15, -3, 5, 13, -11, 7, 6, -4, 2, 11, -5, 7, 12, -11, -15, 1, -1, -9, 10, -8, 1, 2, 8, 11, -14, -4,
            -3, -12, -2, 8, 5, -1, -9, -4, -3, -13, -12, -12, -10, -3, 6, 1, 12, 3, -3, 12, 11, 11, 10]
    nums = [0, 0, 0]

    test = Solution()
    print(test.threeSum(nums=nums))

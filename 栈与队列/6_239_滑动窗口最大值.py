from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = nums[:k - 1]
        result = []
        for i in range(k - 1, len(nums)):
            stack.append(nums[i])
            result.append(max(stack))
            stack.pop(0)

        print(result)
        return result


if __name__ == '__main__':
    so = Solution()
    so.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=1)

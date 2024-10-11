from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[:i + k]))
        print(result)
        return result


if __name__ == '__main__':
    so = Solution()
    so.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)

def minSubArrayLen(target, nums):
    l = len(nums)
    left = 0
    right = 0
    sum = 0
    min_len = float('inf')
    while right < l:
        sum = sum + nums[right]
        while sum >= target:
            print(right, left)
            min_len = min(min_len, right - left + 1)
            sum = sum - nums[left]
            left = left + 1
        right = right + 1
    print(min_len)


if __name__ == '__main__':
    minSubArrayLen(nums=[2, 3, 1, 2, 4, 3], target=7)

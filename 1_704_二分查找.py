def search(nums, target) -> int:
    left, right = 0, len(nums) - 1  # 定义数组的最小下标和最大下标
    while left <= right:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1


if __name__ == '__main__':
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))
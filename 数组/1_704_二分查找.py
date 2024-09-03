def search(nums, target) -> int:
    left, right = 0, len(nums) - 1  # 定义左右指针
    while left <= right:
        middle = (right + left) // 2  # 每个while循环都计算一次中间指针
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


if __name__ == '__main__':
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=9))
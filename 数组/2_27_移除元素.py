def removeElement(nums, val):
    fast = 0  # 初始快指针
    slow = 0  # 初始慢指针
    size = len(nums)

    while fast < size:  # 当fast还没排除完时
        if nums[fast] != val:  # 哥哥发现当前是好瓜
            nums[slow] = nums[fast]  # 将瓜给弟弟
            slow += 1  # 弟弟去下一个瓜坑等着
        fast += 1  # 哥哥也去下一个瓜坑等着
    return slow


if __name__ == '__main__':
    print(removeElement(nums=[-1, 0, 3, 5, 9, 12], val=9))

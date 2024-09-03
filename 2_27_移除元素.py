def removeElement(nums, val):
    # 快慢指针
    fast = 0  # 快指针
    slow = 0  # 慢指针
    size = len(nums)
    while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
        # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
        if nums[fast] != val: # 相当于对一个列表做两次记录，后一次的记录回更新当前的列表，哥哥排除烂瓜给弟弟好瓜
            nums[slow] = nums[fast]
            slow = slow + 1
        fast = fast + 1
    return slow


if __name__ == '__main__':
    print(removeElement(nums=[-1, 0, 3, 5, 9, 12], val=9))

def intersection(nums1, nums2):
    # 使用hash表，字典也是一种哈希表，同样的还有数组，set
    table = {}

    for i in nums1:
        table[i] = table.get(i, 0) + 1  # 这里很巧妙，用nums1的值当作哈希表的key,哈希表的value用来记录出现的频率
    print(table)

    # 自己想的一种
    # res = set()
    # for i in nums2:
    #     table[i] = table.get(i, 0) - 1
    #
    # for key,val in table.items():
    #     if val==0:
    #         res.add(key)
    #
    # print(res)
    res = set()
    for i in nums2:
        if i in table:  # 这里比较的应该是i在不在key里
            res.add(i)
            del table[i]
    print(res)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 2, 2, 6, 7, 8, 9]
    nums2 = [7, 8, 9, 10, 11, 12, 13, 14]

    intersection(nums1, nums2)

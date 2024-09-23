# 将4组数，两两分成两组来求和
def fourSumCount(nums1, nums2, nums3, nums4):
    hashmap1 = dict()
    for i in nums1:
        for j in nums2:
            if i + j not in hashmap1:
                hashmap1[i + j] = 1
            else:
                hashmap1[i + j] = hashmap1[i + j] + 1

            # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
    count = 0
    for n3 in nums3:
        for n4 in nums4:
            key = - n3 - n4
            if key in hashmap1:
                count += hashmap1[key]
    return count
# hashmap2 = dict()
# for i in nums3:
#     for j in nums4:
#         if i + j not in hashmap2:
#             hashmap2[i + j] = 1
#         else:
#             hashmap2[i + j] = hashmap2[i + j] + 1
# count = 0
# for k1, value1 in hashmap1.items():
#     for k2, value2 in hashmap2.items():
#         if k1 + k2 == 0:
#             count = count + (value1 * value2)
#
# print(count)


if __name__ == '__main__':
    print(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))

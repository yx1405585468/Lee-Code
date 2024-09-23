from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    records = dict()
    for index, value in enumerate(nums):  # 把下标和value分离开并存储
        if target - value in records:
            return [records[target - value], index]
        records[value] = index
    return []


if __name__ == '__main__':
    print(twoSum([1, 3, 5, 7, 9], 16))

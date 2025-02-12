from typing import List


class Solution:
    # 双指针
    def reverseStr(self, s: List[str], k: int) -> List[str]:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """

        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)
        for cur in range(0, len(s), 2 * k):  # 每次步进2k就行了，将前k个处理了
            res[cur:cur + k] = reverse_substring(res[cur: cur + k])


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    so = Solution()
    so.reverseStr(s, k=2)

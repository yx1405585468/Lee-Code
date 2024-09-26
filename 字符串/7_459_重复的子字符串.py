class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.get_next(s)

    def get_next(self, s):
        result = [0] * len(s)

        for j in range(1, len(s)):
            i = 0
            location = j
            k = 0
            while s[i] == s[j] and i < j:
                k += 1
                i += 1
                j -= 1
            result[location] = k
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.repeatedSubstringPattern("abcabcabcabc"))

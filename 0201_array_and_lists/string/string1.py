class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        max_str = ''
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            str_set = set(s[i] for s in strs)
            if len(str_set) > 1:
                break

            max_str += list(str_set)[0]

        return max_str


strs = ["flower", "flow", "flight"]
s = Solution()
assert s.longestCommonPrefix(strs=strs) == "fl"

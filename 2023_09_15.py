# 固定长度滑动窗口代码模板 Fixed length sliding window code template
import collections
from typing import List

nums = [1, 2, 3, 4, 5]
window_size = 2
left = 0
right = 0
window = collections.deque()
while right < len(nums):
    window.append(nums[right])
    if right - left + 1 > window_size:
        window.popleft()
        left += 1
    right += 1

# 大小为 K 且平均值大于等于阈值的子数组数目
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = 0
        window_sum = 0
        ans = 0
        while right < len(arr):
             window_sum += arr[right]
             if right - left + 1 >= k:
                 if window_sum >= k * threshold:
                     ans += 1
                 window_sum -= arr[left]
                 left += 1
             right += 1
        return ans

# 不定长度滑动窗口代码模板 Indefinite length sliding window code template
"""
left = 0
right = 0

while right < len(nums):
    window.append(nums[right])

    while 窗口需要缩小:
        # ... 可维护答案
        window.popleft()
        left += 1

    # 向右侧增大窗口
    right += 1
"""
# 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = dict()
        ans = 0
        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            while window[s[right]] > 1: #此while结束后right更新
                window[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans









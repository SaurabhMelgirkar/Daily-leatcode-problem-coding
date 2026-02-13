# print("hi")
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count1 = 0
        max_length = 0
        current_substring = ""
        for i in s:
            if i not  in current_substring:
                current_substring+=i
                count1+=1
                max_length=max(max_length,count1)
            else:
                count1 = len(current_substring[current_substring.index(i) + 1:]) + 1
                current_substring = current_substring[current_substring.index(i) + 1:] + i
            
            print(current_substring)
            print(count1)

        return max_length
s=Solution()
res=s.lengthOfLongestSubstring("pwwkew")
print(res)
r=s.lengthOfLongestSubstring("abcabcbb")
print(r)
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count1 = 0
        max_length = 0
        current_substring = ""
        
        for i in s:
            if i not in current_substring:
                current_substring += i
                count1 += 1
                max_length = max(max_length, count1)
            else:
                count1 = len(current_substring[current_substring.index(i) + 1:]) + 1
                current_substring = current_substring[current_substring.index(i) + 1:] + i
            
            print(current_substring)
            print(count1)

        return max_length

# Example usage:
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # Output: 3
print(s.lengthOfLongestSubstring("bbbbb"))    # Output: 1
print(s.lengthOfLongestSubstring("pwwkew"))   # Output: 3

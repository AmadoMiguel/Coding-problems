# Given a string, find the length of the longest substring without repeating characters.

# Here is an example solution in Python language. (Any language is OK to use in an interview, 
# though we'd recommend Python as a generalist language utilized by companies like Google, Facebook,
# Netflix, Dropbox, Pinterest, Uber, etc.,)

# Can you find a solution in linear time?

class Solution:
  def lengthOfLongestSubstring(self, s):
    curr_len,curr_substr,curr_longest,curr_longest_len = 0,"","",0
    for c in s:
        if curr_len == 0:
            curr_substr += c
            curr_len += 1
            continue
        not_present = True
        # Check if the current character is present in current evaluated
        # substring. If so, remove the substring up to that point and add
        # the new character to conform the new current substring
        for i in range(curr_len):
            if curr_substr[i] == c:
                not_present = False
                if curr_len > curr_longest_len:
                    curr_longest_len = curr_len
                    curr_longest = curr_substr
                curr_substr = curr_substr[i+1:] + c
                curr_len -= i
                break
        if not_present:
            curr_substr += c
            curr_len += 1
    return curr_longest,curr_longest_len

print(Solution().lengthOfLongestSubstring('abrkaabecdefghijkkjxxx'))
# # 10
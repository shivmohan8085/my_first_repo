# def longest_substring_length(s):
#     max_length = 0
#     left = 0
#     seen = {}
    
#     for right, char in enumerate(s):
#         if char in seen:
#             left = max(left, seen[char] + 1)
#         seen[char] = right
#         max_length = max(max_length, right - left + 1)
    
#     return max_length

# # Example usage:
# s = "abcabcbb"
# print(longest_substring_length(s))  # Output should be 

# s = "abcabcbb"
# subs = []
# for char in s :
#     if not char in subs:
#         subs.append(char)
# mains = str(subs)
# print(len(mains))

#------------------------------
s = str(input())
if (s.startswith('(') and s.endswith(')')):
    print("true")
else:
    print("false")



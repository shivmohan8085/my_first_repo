# str = input("enter:")

# for i in range(97,123):
#     count = 0
#     j = chr(i)
#     for x in str:
#         if j == x :
#             count += 1
    
#     if count >0:
#         print(j,":",count)

# # String
# input_string = "hello, world!"

# # Dictionary to store frequency



# frequency_dict = {}

# # Count the occurrences of each character in the string
# for char in input_string:
#     if char in frequency_dict:
#         frequency_dict[char] += 1
#     else:
#         frequency_dict[char] = 1

# # Display the result
# for char, count in frequency_dict.items(): 
#     if char !=" ":
#         print(f"The character '{char}' appears {count} times in the string.")





#------------------------


# # String
# input_string = "hello, world!"

# # Dictionary to store character frequencies
# char_frequency = {}

# # Find the character with the highest occurrence
# max_char = ''
# max_occurrence = 0

# for char in input_string:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
    
#     if char_frequency[char] > max_occurrence:
#         max_char = char
#         max_occurrence = char_frequency[char]

# # Display the result
# print(f"The character '{max_char}' has the highest occurrence ({max_occurrence} times) in the string.")


#--------------------------

# str = "shivmohan shrama"
# v = ['a','e','i','o','u']
# x =[]
# for i in str :
#     if i in v :
#         print(i,end =" ")
# print()


#-------------------------------------------------

l = [1,2,4,5,2,3,6]
l.sort()
print(l)
print("&&&&&&&&&&&&&")

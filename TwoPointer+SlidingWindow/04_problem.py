# Longest Substring Without Repeating Chars
# brute force approach


# findString = "abcabcbb"

# def longestSubString(findString):

#     try:
#             longestString = ""
#             n = len(findString)
#             for i in range(n):
#                 for j in range(i + 1, n + 1):
#                     subStr = findString[i:j]
#                     uniqueSet = set(subStr)
#                     if len(subStr) == len(uniqueSet):
#                         if len(subStr) > len(longestString):
#                             longestString = subStr
#                             print("uni",longestString)
          
#     except Exception as err:
#          print(f"An error occurred: {err}")

# longestSubString(findString)



# brute force approach




findString = "abcabcbb"

def longestSubString():
    try:
        right = 0
        left = 0
        maxLength = 0
        result = ""

        strLenth = len(findString)
        for i in range(strLenth):
            window = findString[left:right + 1]
            right += 1
            uniqueSet = set(window)
            if len(window) == len(uniqueSet):
                if len(window) > maxLength:
                    maxLength = len(window)
                    result = window
        print("res", result)
    except Exception as err:
        print(f"Error Occured", {err})

longestSubString()
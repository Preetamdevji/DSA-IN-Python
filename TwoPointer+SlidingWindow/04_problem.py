# Longest Substring Without Repeating Chars

findString = "abcabcbb"

def longestSubString(findString):

    n = len(findString)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subStr = findString(n[i:j])
            print("subStr", subStr)
            
        

longestSubString(findString)
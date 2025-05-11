# Brute Force Approach

# nums = [1, 2, 3, 4, 1]
# # nums = [1, 2, 3, 4, 5]


# def containDuplicate(nums):

#     try:
    
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1 , n):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
#     except Exception as err:
#         print(f"Error Occured {err}")    
   

# print(containDuplicate(nums))


# hashing approach
# HashSet Method
# time complexity O(n)

nums = [1, 2, 3, 4, 1]

def checkingDuplicate(nums):
    try:
        uniqueElement = set()
        n = len(nums)
        print(uniqueElement)
        for i in range(n):
            print(f"Element: {nums[i]}, Hash: {hash(nums[i])}")
            if nums[i] in uniqueElement:
                return True
            else:
                uniqueElement.add(nums[i])
        return False
            
    except Exception as err:
        print(f"Error Occured {err}")

print(checkingDuplicate(nums))
# Brute Force Approach:
# Intersection of Two Arrays
# Time complexity 
# Outer Loop Big O(n)
# Inner Loop Big O(n)
# Total Time Complexity O(n X m)

nums1 = [1, 2, 2, 1]  
nums2 = [2, 2]


def checkingCommanValue(nums1,nums2):

    try:
        uniqueElement = set()
        for i in range(len(nums1)):
            for j in range(i, len(nums2)):
                if nums1[i] == nums2[j]:
                    uniqueElement.add(nums1[i])
            return uniqueElement
    except Exception as err:
        print(f"Error Occured {err}")

checkingCommanValue(nums1,nums2)



# Hashing Approach
# Intersection of Two Arrays
# Time complexity 
# Big O(n)



nums1 = [1, 2, 2, 1]  
nums2 = [2, 2]


def checkingCommanValue(nums1,nums2):

    try:
        uniqueElement1 = set(nums1)
        uniqueElement2 = set(nums2)
        result = []

        for element1 in uniqueElement1:
            if element1 in uniqueElement2:
                result.append(element1)
            return result 
    except Exception as err:
        print(f"Error Occured {err}")

checkingCommanValue(nums1,nums2)
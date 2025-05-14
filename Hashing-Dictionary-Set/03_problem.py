# brute force
# Intersection of Two Arrays II
# ⏱ Time Complexity:
# Outer loop → O(n)
# Inner loop → O(m)
# Total = O(n * m)


nums1 = [1, 2, 2, 1]  
nums2 = [2, 2]


def checkingCommonWithFrequencyCount(nums1,nums2):
    try:
        result = []
        visted_list = [False] * len(nums2)
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and not visted_list[j]:
                    result.append(nums1[i])
                    visted_list[j] = True
                    break
        print(result)  
    except Exception as err:
        print(f"Error Occured {err}")

checkingCommonWithFrequencyCount(nums1,nums2)





# Hashing Approach (HashMap)
# Intersection of Two Arrays II
# ⏱ Time Complexity:
# Outer loop → O(n)
# Total = O(n + m)


nums1 = [1, 2, 2, 1]  
nums2 = [2, 2]


def checkingCommonWithFrequencyCount(nums1,nums2):
    try:
        result = []
        frequencyCount = {}
        
        for num in nums1:
            if num in frequencyCount:
                frequencyCount[num] += 1
            else: 
                frequencyCount[num] = 1       

        for num in nums2:
            if num in frequencyCount and frequencyCount[num] > 0:
                result.append(num)
                frequencyCount[num] -= 1

        print(result)
    except Exception as err:
        print(f"Error Occured {err}")

checkingCommonWithFrequencyCount(nums1,nums2)
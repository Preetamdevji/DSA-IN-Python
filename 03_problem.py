# first approach brute force 
# Max Sum Subarray of Size K

# nums: list = [1,5,4,2,9,9,9] 
# k: int = 3

# def maximumSubArraySum(nums):
#     try:
#         maxSum = float('-inf')

#         for i,num in enumerate(nums):
#             if i + k <= len(nums):s
#                 currentSum = sum(nums[i:i + k])  
#                 maxSum = max(maxSum, currentSum) 
#         print("Maximum subarray sum of size", k, "is:", maxSum)
#     except Exception as e:
#         print(f"An error occurred: {e}")
    

# maximumSubArraySum(nums)


# second approach Sliding Window

# nums: list = [1,5,4,2,9,9,9] 
# k: int = 3


# def maximunSumOfSubArray(nums):
        
#     window_Sum = sum(nums[:k])
    
#     for i in range(1, len(nums) - k + 1):
#         window_Sum = window_Sum - nums[i - 1] + nums[i + k - 1]
#     print("window_Sum", window_Sum)
        

# maximunSumOfSubArray(nums)

# challenge part same element cannot plus 
nums: list = [1,5,4,2,9,9,9] 
k: int = 3

def maximunSumOfSubArray(nums):
        
    window_Sum = sum(nums[:k])
    
    for i in range(1, len(nums) - k + 1):
        if nums[i - 1] != nums[i + k - 1]:
            window_Sum = window_Sum - nums[i - 1] + nums[i + k - 1]
    print("window_Sum", window_Sum)
        

maximunSumOfSubArray(nums)
# Task is to find the contiguous subarray (must be one piece, no skipping elements) that has the maximum sum — and return that sum.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def checkMaximumNumber(numbers):
    currentNumber = 0
    maxSum = 0
    for nums in numbers:
        currentNumber = max(currentNumber + nums, nums)
        maxSum = max(maxSum, currentNumber)
        print(maxSum,currentNumber)


checkMaximumNumber(numbers)
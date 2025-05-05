# Task is to find the contiguous subarray (must be one piece, no skipping elements) that has the maximum sum — and return that sum.


def checkMaximumNumber(numbers):
    currentNumber = numbers[0]
    maxSum = numbers[0]

    for nums in numbers[1:]:
        currentNumber = max(currentNumber + nums, nums)
        maxSum = max(maxSum , currentNumber)

    return maxSum

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
results = checkMaximumNumber(numbers)
print("Maximum number: ", results)
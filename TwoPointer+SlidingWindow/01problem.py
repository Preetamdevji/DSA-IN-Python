import time
# # first approach Brute Force

# # Time Complexcity Big O(n X n = n2)

# List of numbers
# nums = [
#     12, 25, 36, 48, 6, 29, 14, 10, 30, 41,
#     9, 17, 50, 38, 21, 8, 15, 43, 11, 3,
#     13, 22, 37, 40, 2, 34, 20, 27, 31, 19,
#     7, 39, 5, 18, 4, 24, 28, 35, 26, 16,
#     23, 45, 1, 0, 47, 32, 46, 44, 33, 49,
#     6, 14, 29, 12, 30, 19, 3, 21, 25, 36,
#     9, 13, 24, 8, 10, 17, 7, 15, 11, 2,
#     26, 22, 5, 28, 31, 41, 23, 20, 27, 34,
#     38, 16, 18, 1, 40, 4, 39, 33, 0, 50,
#     45, 35, 46, 32, 43, 44, 37, 47, 49, 48
# ]
# targetEqual = 60

# # Function to check if there is a pair with sum equal to targetEqual
# def has_pair_with_sum(nums, targetEqual):
#     numsLength = len(nums)
#     for i in range(numsLength):
#         for j in range(i + 1, numsLength):
#             if nums[i] + nums[j] == targetEqual:
#                 print(f"Pair found: {nums[i]} + {nums[j]} = {targetEqual}")
#                 return True
#     return False

# # Timing the brute-force solution
# start_time = time.time()

# # Call the function
# result = has_pair_with_sum(nums, targetEqual)

# end_time = time.time()

# # Print the result and the time taken
# print("Result:", result)
# print("Execution time:", end_time - start_time, "seconds")


# Time Complexity Optimize way
# Big O(n)



nums = [
    12, 25, 36, 48, 6, 29, 14, 10, 30, 41,
    9, 17, 50, 38, 21, 8, 15, 43, 11, 3,
    13, 22, 37, 40, 2, 34, 20, 27, 31, 19,
    7, 39, 5, 18, 4, 24, 28, 35, 26, 16,
    23, 45, 1, 0, 47, 32, 46, 44, 33, 49,
    6, 14, 29, 12, 30, 19, 3, 21, 25, 36,
    9, 13, 24, 8, 10, 17, 7, 15, 11, 2,
    26, 22, 5, 28, 31, 41, 23, 20, 27, 34,
    38, 16, 18, 1, 40, 4, 39, 33, 0, 50,
    45, 35, 46, 32, 43, 44, 37, 47, 49, 48
]
targetEqual = 60

# Function to check if there is a pair with sum equal to targetEqual
def has_pair_with_sum(nums, targetEqual):
    try:
        mySet = set()
        numsLength = len(nums)

        for i in range(numsLength):
            mySet.add(nums[i])
            complement = targetEqual - nums[i]
            if complement in mySet:
                print(f"Pair found: {complement} + {nums[i]} = {targetEqual}")
                return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")

# Measure time
start_time = time.time()

# Call the function and print the result
result = has_pair_with_sum(nums, targetEqual)

end_time = time.time()

# Print the result and execution time
print("Result:", result)
print("Execution time:", end_time - start_time, "seconds")

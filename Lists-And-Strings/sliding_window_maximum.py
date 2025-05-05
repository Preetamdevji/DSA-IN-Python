from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

def max_in_sliding_window(nums, k):

    deq = deque()
    result_max_number = []

    for i in range(len(nums)):
        # Step 1: Remove out-of-window indices
        # print(i - k + 1)
        # deque store index

        if deq and deq[0] < i - k + 1:  
            removed = deq.popleft()
            print("Removed from front (out of window):", removed)
        # step 2: Maintain decreasing order
        # nums[deq[-1]] -> means last element deque ka
        # nums[i] means current element
        while deq and nums[deq[-1]] < nums[i]:
            removed = deq.pop()
            print("Removed from back (smaller than current):", removed)

         # Step 3: Add current index
        deq.append(i)
        print("Appended:", i, "→ dq:", list(deq))

        # Step 4: Add to result if window is full
        if i > k - 1:
            max_val = nums[deq[0]]
            result_max_number.append(max_val)
            print("Current max:", max_val)
    print("Final result:", result_max_number)
        
max_in_sliding_window(nums, k)













# def max_in_sliding_window(nums, k):
#     dq = deque()
#     result_max_number = []

#     for i in range(len(nums)):
#         # Step 1: Remove out-of-window indices
#         if dq and dq[0] < i - k + 1:
#             removed = dq.popleft()
#             print("Removed from front (out of window):", removed)

#         # Step 2: Maintain decreasing order
#         while dq and nums[dq[-1]] < nums[i]:
#             removed = dq.pop()
#             print("Removed from back (smaller than current):", removed)

#         # Step 3: Add current index
#         dq.append(i)
#         print("Appended:", i, "→ dq:", list(dq))

#         # Step 4: Add to result if window is full
#         if i >= k - 1:
#             max_val = nums[dq[0]]
#             result_max_number.append(max_val)
#             print("Current max:", max_val)

#     print("Final result:", result_max_number)

# max_in_sliding_window(nums, k)

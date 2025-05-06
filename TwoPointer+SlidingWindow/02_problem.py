# Move Zeros to End

# first approach Big O(n)

nums = [0, 1, 0, 3, 12]

def rearrangeNum(nums):

    index = 0 
    # First loop: Move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            nonZeroElement = nums[index]
            index += 1
            print(nonZeroElement)

    for j in range(index, len(nums)):
        record = nums[j] = 0
        print("numJ", record)


rearrangeNum(nums)
print(nums)
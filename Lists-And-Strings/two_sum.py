# Task is to find two numbers in the list that add up to the target number, and return their indices (positions in the list).

number_list = [1, 6, 3, 2]
target_number = 8


def twoSum(number_list):
    memory = {}
    for index,num in enumerate(number_list):
        needValue = target_number - num
        # storeValue = {needValue}
        if needValue in memory:
            print(f"Cool. I’ll remember this number: {num} at index {index}")
            print(f"Indices: {memory[needValue]} and {index}")
            return
        else:
            print("Boom! The match has been seen earlier — you’ve found your pair!")
            memory[num] = index
        

twoSum(number_list)


numbers = [100, 4, 200, 1, 3, 2, 5]

numbers_set = set(numbers)
longest_streak = 0

print(numbers_set)


for nums in numbers_set:
    if (nums - 1) not in numbers_set:
        current_num = nums
        current_streak = 1
        
        while (current_num + 1) in numbers_set:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)
        
print(longest_streak)

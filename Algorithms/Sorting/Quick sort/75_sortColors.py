class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Initialize pointers for the next position of 0, the next position of 2, and the current element
        next_zero_index, next_two_index, current_index = -1, len(nums), 0

        # Process elements until the current_index reaches the next_two_index
        while current_index < next_two_index:
            if nums[current_index] == 0:
                # Move the 0 to the next position for 0
                next_zero_index += 1
                nums[next_zero_index], nums[current_index] = nums[current_index], nums[next_zero_index]
                # Move to the next element
                current_index += 1
            elif nums[current_index] == 2:
                # Move the 2 to the next position for 2
                next_two_index -= 1
                nums[next_two_index], nums[current_index] = nums[current_index], nums[next_two_index]
                # Do not increment current_index because we need to check the newly swapped element
            else:
                # If the current element is a 1, just move to the next element
                current_index += 1
        # The function modifies the list in place, so there is no return value
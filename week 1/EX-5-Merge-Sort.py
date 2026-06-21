# Merge Sort Implementation

def merge_sort(numbers):
    if len(numbers) > 1:
        # Find middle index
        middle = len(numbers) // 2
        # Divide array into two halves
        left_half = numbers[:middle]
        right_half = numbers[middle:]
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        left_index = 0
        right_index = 0
        merged_index = 0

        # Merge the sorted halves
        while (left_index < len(left_half)
               and right_index < len(right_half)):
            if left_half[left_index] < right_half[right_index]:
                numbers[merged_index] = left_half[left_index]
                left_index += 1
            else:
                numbers[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1
        # Copy remaining elements from left half
        while left_index < len(left_half):
            numbers[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1
        # Copy remaining elements from right half
        while right_index < len(right_half):
            numbers[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

numbers = [38, 27, 43, 3, 9, 82, 10]
print("Before Sorting:", numbers)
merge_sort(numbers)
print("After Sorting:", numbers)


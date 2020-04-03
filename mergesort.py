def merge(left, right):
    sorted = []
    left_index = right_index = 0
    left_length, right_length = len(left), len(right)
    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left[left_index] <= right[right_index]:
                sorted.append(left[left_index])
                left_index += 1
            else:
                sorted.append(right[right_index])
                right_index += 1
        elif left_index == left_length:
            sorted.append(right[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted.append(left[left_index])
            left_index += 1
    return sorted
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)
def merge_sort_main():
    my_text = ""
    with open("C:\Lol\inum.txt") as f:
        for line in f:
            text = line
            my_text += " " + text
    my_list = text.split()
    my_list = [int(i) for i in my_list]
    print(merge_sort(my_list))
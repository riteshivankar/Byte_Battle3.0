#Problem 1
# Write a  program to find the middle element of the list. If the list contains an even number of elements, return the second middle element.
def find_middle(lst):
    length = len(lst)
    if length % 2 == 0:  # if the length is even
        middle_index = length // 2
        return lst[middle_index]  # return the second  middle elements
    else:  # if the length is odd
        middle_index = length // 2
        return lst[middle_index]  # return the middle element


# Example usage:
my_list = [1, 2, 3, 4, 5]
result = find_middle(my_list)
print("Middle element (odd string):", result)

my_list = [1, 2, 3, 4, 5 ,6]
result = find_middle(my_list)
print("Second Middle element of even string :", result)
# List comprehension method
# min() can be applied to strings
def first_string(str_lst):
    return min([string.replace(' ', '') for string in str_lst])

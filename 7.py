list_of_nums = [1, 2, 3] # создаём список
def is_list(value):
    return isinstance(value, list)
is_list(list_of_nums)  # True
is_list('string')  # False

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3, "boy", False)
print_params(3, 3, 3)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [5.5, True, "string"]
values_dict = {'a': 78, 'b': "food", 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['dog', 32.2]
print_params(*values_list_2, 42)


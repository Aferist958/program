def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 2, 3)
print_params(5, 1, 7)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [True, 2, 'str']
values_dict = {'a': 1, 'b': 2, 'c': 3}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'tttt']

print_params(*values_list_2, 42)

immutable_var = ([0, 1], True, 'string')
print(immutable_var)
immutable_var[0][0] = 2
#immutable_var[1] = 1 не будет работать, потому что кортеж не изменяемый тип данных
mutable_list = [False, 0, 'list']
mutable_list[0] = True
print(mutable_list)
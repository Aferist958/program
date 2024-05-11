grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
dict_ = dict(zip(students, grades))
dict_variable = {key:sum(value)/len(value) for key, value in dict_.items()}
print(dict_variable)

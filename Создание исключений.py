
class Car:
    def __init__(self, model, vin_number , numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers


        def __is_valid_vin(vin_number):
            if isinstance(vin_number, float) == True:
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if not(9999999 >= vin_number >= 1000000):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return True



        def __is_valid_numbers(numbers):
            if isinstance(numbers, str) == False:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if not(len(numbers) == 6):
                raise IncorrectVinNumber('Неверная длина номера')
            return True

        __is_valid_vin(vin_number)
        __is_valid_numbers(numbers)

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message






try:
  first = Car('Model1', 100000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
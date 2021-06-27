#tuplas, além de listas imutáveis são também registros
fortaleza_coordinates = (-3.71839,-38.5434)
visitor_check_in = ('Thiago Beppe', 26, "Casado", "Engenheiro de dados")
numbers_list = (i for i in range(0,5))

#Desempacotamento
latitude, longitude = fortaleza_coordinates
print(latitude)
print(longitude)
print("Nome : %s, Idade: %d, Estado Civil: %s, Profissão: %s" % visitor_check_in)

first_value, second_value, *rest = numbers_list
print(first_value)
print(second_value)
print(rest)

#Tuplas Nomeadas
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')

tokyo = City("tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.coordinates)
print(City._fields)
print(tokyo._asdict())
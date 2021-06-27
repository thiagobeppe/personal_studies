# Diferenças entre for e list compreenhision

string_example = 'ABC'
dummy_list_standart = []
for letter in string_example:
    dummy_list_standart.append(ord(letter))
print(dummy_list_standart)

# Sempre que voce precisar criar novas listas e não precisa performar algo complexo use listcomp 
dummy_list_listcomp = [ord(letter) for letter in string_example]
print(dummy_list_listcomp)

#ListComps para produtos cartersianos
sizes = ['S','M','L', 'XL']
collors = ['white','black','purple', 'pink']

tshirts_combination_by_size = [(collor,size) for size in sizes for collor in collors]
print(tshirts_combination_by_size)

tshirts_combination_by_collor = [(collor,size) for collor in collors for size in sizes ]
print(tshirts_combination_by_collor)
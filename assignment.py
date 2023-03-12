///Text type

str= 'kisa'
str='test'
del str
print(str)

 # Numeric Type (Numbers, floats , complex)
int1 = 7
print(int1)
my_int = 15
del int1

float1 = 3.24
print(float1)
float1 = 10.01
del float1

complex1 = 4 + 5j
print(complex1)
complex1 = 1 + 7j
del complex1

#list

list1 = [a, b, c, d, e]
print(list1)
list1[3] = x
del my_list

#Tupple
tuple2 = (1, 2, 3, 4, 5)
print(tuple2)

# Update - Since ,tuples are immutable, so we cannot update elements as an indivual
# Therefore, we create a new tuple with the updated values

my_tuple = (10, 20, 30, 40, 50)
del tuple2

#range
range1 = range(0, 20)
print(list(range1))

# Update - Ranges are immutable, so we cannot update elements as an indivual
# Instead, we need to create a new range with the updated values

range1 = range(0, 30)
del range1


#Dictionary
my_dict = {'name': 'Kisa', 'age': 26, 'company': '10Pearls'}
print(my_dict)
my_dict['name'] = Kisa Abidi
del my_dict
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
my_set.clear()

#Frozenset
my_frozenset = frozenset({1, 2, 3, 4, 5})
print(my_frozenset)

# Update - Frozensets are immutable, so we cannot update individual elements
# Instead, we need to create a new frozenset with the updated values
new_frozenset = frozenset({6, 7, 8, 9, 10})
del my_frozenset


#Bool
bool1 = True
print(bool1)
bool1 = False
del bool1


#byte
my_bytes = b'Hello World'
print(my_bytes)

# Update - Bytes are immutable, so we cannot update individual elements
# Instead, we need to create a new bytes object with the updated values
new_bytes = b'learning Selenium'
del my_bytes


#byteArray
my_bytearray = bytearray(b'Bye Bye')

#None
x = None
print(x)




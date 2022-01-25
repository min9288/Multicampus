'''
    Tuple
'''

my_tuple = (1,2,3)
print(type(my_tuple), my_tuple)

# my_tuple[1] = 4
# TypeError: 'tuple' object does not support item assignment

value = (4)
value2 = (4, )
print(type(value), type(value2))

def swap(a, b):
    return (b, a)

print(type(swap(10, 20)))
print(swap(10, 20))

a, b = swap(10, 20)
print(f'a = {a}, b = {b} ')

'''
    Set - Unique value (중복 허용하지 않음)
'''
my_set = list([10,20,40,20,30,10])
print(type(my_set), my_set)
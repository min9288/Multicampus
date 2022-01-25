'''
    function : default value
'''
def my_func(a=20, b=10):
    return a - b

print(my_func())
print(my_func(30))
print(my_func(40, 5))

def my_func2(a, b=10):
    return a + b

# default parameter value가 non-default paramter 보다 먼저 올 수 없다.
# def my_func3(a=20, b):
#     return a + b

'''
    function : tuple parameter, dict parameter
'''
def my_func_tuple(*p):
    return p

print(type(my_func_tuple(10)))
print(my_func_tuple(10, 20, 30))

def my_func_dict(**p):
    for k,v in p.items():
        print(f'key = {k}, value = {v}')

my_func_dict(a=1, b=2, c=3)


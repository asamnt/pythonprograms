def my_decorator(func):
    def inner():#getting decorated here
        print('before func')
        func()#actual function getting called here
        print('after func')

    return inner

@my_decorator
def some_func():
    print('hey you guys')

print('some func()')

some_func()
'''
print('')

some_func_decorated = my_decorator(some_func)

print('some_func with decorator')

some_func_decorated()
'''
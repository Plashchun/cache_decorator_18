def cache_decorator(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if (args, tuple(kwargs.items())) in cache_dict:
            return cache_dict[(args, tuple(kwargs.items()))]
        else:
            result = func(*args, **kwargs)
            cache_dict[(args, tuple(kwargs.items()))] = result
            return result
    return wrapper
@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b

@cache_decorator
def circle_area(r: float) -> float:
    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r * r)

print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
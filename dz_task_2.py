# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def dict_kwargs(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set, bytearray)):
            value = str(value)
        result_dict[value] = key
    return result_dict

print(dict_kwargs(res=1, reverse=[1, 2, 3], set_one={1, 2, 5, 7}))

from typing import Any
import collections
import re


# Решить задачи, выложить .py файл с решениями на github. В личный кабинет прикрепить .txt файл с ссылкой на профиль.


# Задача 1. Найти количество различных элементов массива. Пример: для [1 4 5 1 1 3] ответ 4.
def count_unique_elems(arr: list[Any]) -> int:
    # использую множество для подсчета уникальных элементов
    return len(set(arr))


# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
def get_10_popular_password(file: str) -> Any:
    pwd_list = []
    with open(file) as f:
        for line in f:
            # загрузка паролей в список
            pwd_list.append(line.split(';')[-1].rstrip('\n'))
    # использую коллекцию для подсчета топ10 паролей
    return collections.Counter(pwd_list).most_common(10)


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
def censor_link(string: str) -> str:
    # регулярное выражение для поиска ссылок
    regex = r'(https?:\/\/)?(www\.)?(\w+\.)+([a-z]{2,})+'
    regex = r'(http[s]?:\/\/)?(\w+\.)+((/\w+)+/?)?'
    return re.sub(regex, '*****', string)


# Здесь писать тесты для функций с решениями
def main():
    arr = [1, 4, 5, 1, 1, 3]
    print(f'Задача 1:\nколичество уникальных элементов массива {arr}: {count_unique_elems(arr)}\n')

    pwd_file = 'pwd.txt'
    print(f'Задача 2:\nколлекция топ10 паролей:\n{get_10_popular_password(pwd_file)}\n')

    print('Задача 3:\n')
    str_with_links = (['www.site.com some. .text taxi.yandex http://example.su vk.ru '
                      'word anotherwordhttp://stackoverflow01.skj44dhf.ru/',
                       'new string ixbt.com 2 34 texttext http://www.amozon.com',
                       'https://pythonworld.ru/https://pythonworld.ru/'])
    for str in str_with_links:
        print(f'результат замены в строке "{str}":\n{censor_link(str)}')


if __name__ == '__main__':
    main()

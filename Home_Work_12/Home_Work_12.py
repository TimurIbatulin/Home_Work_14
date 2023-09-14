# Задание. Создайте класс студента. 
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. 
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). 
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class Examination:
    def __init__(self):
        self.__sum_name = None
    
    def __get__(self, instance, owner):
        return self.__sum_name
    
    def __set__(self, instance, value):
        for i in value:
            if i.isdigit():
                raise ValueError("ОШИБКА! ФИО не может содержать число")
        if not str(value).istitle():
            raise ValueError("OШИБКА! ФИО не ничинается с заглавной буквы")
        self.__sum_name = value

        def __delete__(self, instance):
            del self.__sum_name
        
def scoll_optimization(lessons, scool_class):
    with open(f'scool_{lessons}{scool_class}.csv', 'r', newline = '') as f:
        csv_file = f.read().split('\n')
        print(f'{csv_file = }')
        lessons ={}.fromkeys(csv_file, [])
    return lessons


class StudentLiteLifi:
    _surname = Examination()
    _name = Examination()
    _secondname = Examination()
    def __init__(self, surname, name, secondname, scool_class):
        self._surname = surname
        self._name = name
        self._secondname = secondname
        self._lessons = scoll_optimization('lessons', scool_class)
        self._test = scoll_optimization('test', scool_class)

    # def 


    def __str__(self) -> str:
            return f'фамилия - {self._surname}\nимя - {self._name}\nотчество - {self._secondname}\n{self._lessons}\n{self._test}'


if __name__ == '__main__':
    w = StudentLiteLifi('Ибатулин', 'Тимур', 'Рамилевич', 1)

    print(w)
        

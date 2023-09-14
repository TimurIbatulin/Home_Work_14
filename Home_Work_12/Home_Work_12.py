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
        lessons ={}.fromkeys(csv_file, None)
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

    def estimates_add(self, keys, value):
        w = self._lessons
        if 1 < value < 6:
            if w[keys] == None:
                estimals = []
                estimals.append(value)
            else:
                estimals = w[keys]
                estimals.append(value)
            w[keys] = estimals
            self._lessons = w
        else:
            raise ValueError('Оценка должна быть не меньше 2 и не больше 5')

    def estimates_test_add(self, keys, value):
        w = self._test
        if 0 <= value < 101:
            if w[keys] == None:
                estimals = []
                estimals.append(value)
            else:
                estimals = w[keys]
                estimals.append(value)
            w[keys] = estimals
            self._test = w
        else:
            raise ValueError('Баллы ставятся в диапазоне от 0 до 100')

   
    def test_average_mark(self, key):
        average = self._test[key]
        count = 0
        for i in average:
            count += int(i)
        return f'средний бал по предмету {key} = {count/len(average)}'
    

    def lesson_avenger_mark(self):
        count = 0
        mark = 0
        for i in self._lessons:
            l = self._lessons[i]
            if l != None:
                count += len(l)
                for j in l:
                    mark += int(j)
        if mark > 0:
            return f'Средний бал студента = {mark/count}'
        else:
            return 'Оценок нет'




    def __str__(self) -> str:
            return f'фамилия - {self._surname}\nимя - {self._name}\nотчество - {self._secondname}\n{self._lessons}\n{self._test}'


if __name__ == '__main__':
    w = StudentLiteLifi('Ибатулин', 'Тимур', 'Рамилевич', 1)
    w.estimates_add('Физика', 5)
    w.estimates_add('Русский', 4)
    w.estimates_test_add('Химия', 100)
    w.estimates_test_add('Химия', 100)
    w.estimates_add('Физика', 5)
    print(w.test_average_mark('Химия'))
    print(w.lesson_avenger_mark())
    print(w)
        

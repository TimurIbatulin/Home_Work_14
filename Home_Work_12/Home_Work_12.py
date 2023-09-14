# Задание. Создайте класс студента. 
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. 
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). 
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

class Examination:
    def __init__(self):
        self.__sum_name = None
    
    def __get__(self, instance, owner):
        return self.__sum_name
    
    def __set__(self, instance, value):
        for i in value:
            print(i)
            if i.isdigit():
                raise ValueError("ОШИБКА! ФИО не может содержать число")
        if not str(value).istitle():
            raise ValueError("OШИБКА! ФИО не ничинается с заглавной буквы")
        self.__sum_name = value

        def __delete__(self, instance):
            del self.__sum_name
        
    


class StudentLiteLifi:
    _surname = Examination()
    _name = Examination()
    _secondname = Examination()
    def __init__(self, surname, name, secondname):
        self._surname = surname
        self._name = name
        self._secondname = secondname
    
    def __str__(self) -> str:
            return f'фамилия - {self._surname}\nимя - {self._name}\nотчество - {self._secondname}'


if __name__ == '__main__':
    w = StudentLiteLifi('Ибат5улин', 'Тимур', 'Рамилевич')

    print(w)
        

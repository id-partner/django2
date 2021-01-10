from time import time


# декоратор
def timelog(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Working time is: {round(t2 - t1, 10)} sec')
        return result

    return wrapper


class Product:
    product = 'Product'

    _meta = 'Meta'  # инкаплусяция (Соглашение)
    __meta2 = 'Meta2'  # Строгая инкапсуляция

    @timelog #декоратор
    def add_to_cart(self, count):
        print(1)

    @timelog #декоратор
    def edit_descriotion(self):
        print(2)

    @timelog #декоратор
    def add_review(self, text):
        print(3)


class Book(Product):  # Наследование класса Product
    # атрибуты по умолчанию
    pages = 390
    author = 'Pushkin'

    # конструктор класса
    def __init__(self, name, author, pages):
        self.name = self.product = name  # Наследование классов
        self.author = author
        self.pages = pages

    # магический метод
    def __add__(self, other):
        return Book(
            name=f'{self.name}|{other.name}',
            author=f'{self.author}|{other.author}',
            pages=self.pages + other.pages,
        )

    @timelog #декоратор
    def get_pages_count(self):
        print(f'pages cont in this book: {self.pages}')


"""
инкапсуляция
через нижнее подчеркивание  _meta — служебная. Можно обратиться
через двойное нижнее подчеркивание __meta — служебная. Обратиться уже явно нельзя. Обратиться по названию можно.
Инкапсуляция условная.
"""

"""
Полиморфизм
Можно переобпределять методы родителя у класса потомка.
"""

"""
Магические методы.
Начинаются и заканчиваются с двойного нижнего подчеркивания
например def __init__(self) конструктор
"""

"""
Множественные наследования
Через запятую вписывается, также как и при обычном наследовании
"""

"""
51 минута видео 1
переопределение методов через super
super().функция в род классе
"""

"""
декоратор
обертка, которая добавляет функционал до выполнения функции или/и после выполнения
"""

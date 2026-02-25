'''
В этом задании тебе нужно создать иерархию разных видов фильмов:
драму и комедию, которые наследуются от суперкласса Movies.

    1. Создай класс Movies:
    2. проинициализируй в нём пустой список self.movies через конструктор;
    3. добавь метод add_movie(). Он будет принимать параметр movie и
       добавлять его в конец списка self.movies.
    4. Создай два дочерних класса — Comedy и Drama. 
       Они наследуют метод add_movie(). 
       Метод этих классов должен принимать параметр movie и добавлять его
       в конец списка self.movies.
       Затем возвращать записи вида Комедии: '[]' и Драмы: '[]'
       соответственно.
    5. Вызови метод add_movie() для объекта Comedy(). 
       Входной параметр — 'Большой куш'. Выведи на экран результат.
    6. Вызови метод add_movie() для объекта Drama(). 
       Входной параметр — 'Оружейный барон'. Выведи на экран результат.

Подсказки

    1. Чтобы добавить элемент в конец списка, нужен метод append(). 
       То есть так: self.movies.append(movie).
    2. Чтобы вернуть значение, используй return. 
       Понадобится вернуть значение в определённом виде: 
       return f'Комедии: {self.movies}'.

'''

class Movies:
    def __init__(self, movies):
        self.movies = movies

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def __init__(self, movies):
        super().__init__(movies)

    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def __init__(self, movies):
        super().__init__(movies)

    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


comedies = Comedy([])
print(comedies.add_movie('Большой куш'))

dramas = Drama([])
print(dramas.add_movie('Оружейный барон'))
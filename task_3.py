'''

Нужно написать три класса для спортивных соревнований
— разные способы начислять спортсменам очки:
  1. PointsForPlace — количество очков равно месту,
     которое занял спортсмен.
  2. PointsForMeters — количество очков высчитывается с учётом расстояния,
     на которое спортсмен метнул диск. 
  3. TotalPoints — умеет работать и с местом спортсмена, и с расстоянием.

  
Теперь подробно:

  1. Напиши класс PointsForPlace. 
     Он получает количество очков в зависимости от места,
     которое занял спортсмен.

     В этом классе напиши метод get_points_for_place(), 
     который принимает аргумент place — целое число. Причём: 
       - Если место строго больше 100, должно выводиться сообщение 
         'Баллы начисляются только первым 100 участникам'.
       - Если как аргумент передали значение меньше 1, 
         должно печататься сообщение 
         'Спортсмен не может занять нулевое или отрицательное место'.
       - В остальных случаях начисляются очки по формуле: 101 - place.

     Изначально количество очков равно нулю:
     подумай, как это отобразить в коде. 

     Метод get_points_for_place() должен возвращать points.

  2. Напиши класс PointsForMeters. 
     Он рассчитывает очки в зависимости от количества метров,
     на которое спортсмен толкнул ядро или метнул диск:
       расстояние*0,5. 
     Например, если расстояние 10 метров, спортсмен получит 5 очков.

     Напиши метод get_points_for_meters(), который принимает аргумент
     meters — целое число. Причём:
       - Если количество метров меньше нуля, должно выводиться сообщение
           'Количество метров не может быть отрицательным'.
       - В остальных случаях начисляются очки по формуле:
           «количество метров умножить на 0.5».

     Метод должен возвращать points. Изначально количество очков — 0.

  3. Напиши класс TotalPoints для многоборцев.
     Он наследуется сразу от двух классов 
     — PointsForPlace и PointsForMeters и реализует все их методы.
     Также он должен содержать:
       - метод get_total_points(),
         который принимает как аргументы meters и place;
       - переменную total, которая суммирует значения методов
         get_points_for_place() и get_points_for_meters().

     Метод возвращает переменную total.

     
Важно! 

  Подумай, какие методы в этом задании могут быть статическими.
  Если метод можно сделать статическим — делай.
  Подумай, какая область видимости должна быть у переменной points
  — глобальная или локальная.

Подсказка

  - Чтобы количество очков изначально равнялось нулю,
    используй переменную points = 0.
  - Внутри методов get_points_for_meters() и get_points_for_place)
    должны быть условные операторы. 
    Например, для мест — if place > 100, затем elif place < 1.  


'''


class PointsForPlace:
    @staticmethod
    def get_points_for_place(place: int):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
        return points


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points


class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters: int, place: int):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))


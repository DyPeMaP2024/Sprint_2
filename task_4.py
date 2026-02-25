'''

Напиши класс EmployeeSalary. 
Он рассчитывает почасовую заработную плату сотрудников за неделю.

  1. С помощью переменной hourly_payment 
     установи почасовой уровень оплаты, равный 400.
  2. Проинициализируй атрибуты 
     name, hours, rest_days, email через конструктор.
  3. Добавь метод класса get_hours(). 
     Если значение hours неизвестно, метод  рассчитывает часы,
     исходя из количества выходных — rest_days. 
     Формула для этого случая такая: (7 - rest_days) * 8.
  4. Добавь метод класса get_email(). 
     Если значение email неизвестно, метод генерирует его так:
       f"{name}@email.com".
  5. Добавь метод класса set_hourly_payment().
     Он меняет значение переменной hourly_payment.
  6. Добавь метод расчёта заработной платы salary().
     Формула расчёта такая: hours * hourly_payment.

Подсказки

  - У тебя будет три класс-метода.
    Не забудь, что им всем нужно передать cls в качестве первого аргумента.
  - Метод get_hours() должен вернуть cls:
    return cls(name, hours, rest_days, email). 
    Метод get_email — аналогично. 
    Методу set_hourly_payment() ничего возвращать не нужно,
    потому что он только меняет значение переменной.


'''


class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        hours = self.hours if self.hours is not None else (7 - self.rest_days) * 8
        return hours * self.hourly_payment

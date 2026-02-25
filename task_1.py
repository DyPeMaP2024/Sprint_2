'''
В этом задании тебе нужно создать подвид тест-кейса.

Есть класс Case. Он содержит метод print_test_case_info(), который выводит
на экран id тест-кейса, его название, описание шага, ожидаемый результат. 

Что тебе нужно сделать:

    1. Создай подкласс ExtendedCase. Он наследует все атрибуты из класса
      Case. 
      Кроме того, добавь ему два новых атрибута через конструктор
      — precondition и environment. Тип данных для них — строки.
    2. Вызови метод __init__() суперкласса. Используй функцию super().
    3. Переопредели метод print_test_case_info() в классе ExtendedCase. 
      Он должен печатать:
      - все атрибуты суперкласса;
      - новые атрибуты подкласса в формате "Предусловие: {precondition}" и
      Окружение: {environment}". Каждый атрибут нужно вывести с новой строки.
    4. Создай объект case класса ExtendedCase. Входные параметры такие:
      ('1', 'Наличие кнопки Принять', 
      '1. Открыть вкладку приёма документов 
       2. Проверить наличие кнопки ', 
       'Кнопка доступна', 
       'Открыть сервис', 
       'Яндекс Браузер').
    5. Вызови метод print_test_case_info() для объекта casе.


Подсказки

    Конструктор суперкласса через super() выглядит так: 
      super().__init__(name). Указывать имя суперкласса не нужно.
    
    Чтобы данные выводились с новой строки, используй \n. 
    Например, f"\nПредусловие:  {self.precondition}".
    
    Чтобы вывести все атрибуты суперкласса и добавить ему свои,
    используй super().

'''

class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")

# напиши свой код здесь


class ExtendedCase(Case):
    def __init__(self, test_case_id, name, step_description, expected_result,
                 precondition, environment):
        super().__init__(test_case_id, name, step_description, expected_result)
        self.precondition = precondition
        self.environment = environment

    def print_test_case_info(self):
        super().print_test_case_info()
        print(f"\nПредусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")


case = ExtendedCase(
    '1',
    'Наличие кнопки Принять',
    '1. Открыть вкладку приёма документов\n2. Проверить наличие кнопки ',
    'Кнопка доступна',
    'Открыть сервис',
    'Яндекс Браузер'
)
case.print_test_case_info()

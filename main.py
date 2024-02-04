# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Test:
    def __init__(self, number_of_question: int, number_of_correct: int, grade: int):
        """
        Создание и подготовка к работе объекта "Тест"

        :param number_of_question: Количество вопросов
        :param number_of_correct: Количество верных ответов
        :param grade: Количество верных ответов на оценку отлично

        Примеры:
        >>> test = Test(20, 15, 18)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_question, int):
            raise TypeError("Количество вопросов должно быть типа int")
        if number_of_question < 0:
            raise ValueError("Количество воапросов должено быть неотрицательным числом")
        self.number_of_question = number_of_question

        if not isinstance(number_of_correct, int):
            raise TypeError("Количество правильных ответов должно быть int")
        if number_of_correct < 0:
            raise ValueError("Количество правильных ответов не может быть отрицательным числом")
        self.number_of_correct = number_of_correct

        if not isinstance(grade, int):
            raise TypeError("Количество верных ответов на оценку отлично должно быть типа int")
        if grade < 0:
            raise ValueError("Количество верных ответов на оценку отлично должно быть положительным числом")
        self.grade = grade

    def excellent_mark(self) -> bool:
        """
        Функция которая проверяет является ли тест выполненым на отлично

        :return: Является ли тест выполненым на отлично

        Примеры:
        >>> test = Test(20, 15, 18)
        >>> test.excellent_mark()
        """
        ...

    def incorrect_answer(self, number_of_incorrect: int) -> None:
        """
        Неправильные ответы.

        :param number_of_incorrect: Количество неверных ответов
        :raise ValueError: Если сумма количества верных и неверных ответов превышает количество вопросов
        то возвращается ошибка.

        :return: Количество неверных ответов

        Примеры:
        >>> test = Test(20, 5, 18)
        >>> test.incorrect_answer(15)
        """
        if not isinstance(number_of_incorrect, int):
            raise TypeError("Количество неверных ответов должно быть типа int")
        if number_of_incorrect < 0:
            raise ValueError("Количество неверных ответов должно быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

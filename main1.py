# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Money:
    def __init__(self, savings: float, salary: float):
        """
        Создание и подготовка к работе объекта "Денежные средства"

        :param savings: Накопления
        :param salary: Заработная плата

        Примеры:
        >>> money = Money(30000, 50000)  # инициализация экземпляра класса
        """
        if not isinstance(savings, (int, float)):
            raise TypeError("Накопления должены быть типа int или float")
        if savings < 0:
            raise ValueError("Накопления должены быть положительным числом")
        self.savings = savings

        if not isinstance(salary, (int, float)):
            raise TypeError("Заработная плата должна быть типа int или float")
        if salary < 0:
            raise ValueError("Заработная плата не может быть отрицательным числом")
        self.salary = salary

    def lack_of_money(self) -> bool:
        """
        Функция которая проверяет есть ли денежные средства

        :return: Присутствуют ли денежные средства в наличии

        Примеры:
        >>> money = Money(30000, 50000)
        >>> money.lack_of_money()
        """
        ...

    def the_product_of_expenses(self, expenses: float) -> None:
        """
        Произведение денежных трат.


        :param expenses: Затраты

        :raise ValueError: Если количество затрат превышает сумму имеющихся денежных средств (накоплений и заработной
        платы), то вызываем ошибку

        :return: Количество денежных средств после произведения затрат

        Примеры:
        >>> money = Money(30000, 50000)
        >>> money.the_product_of_expenses(200)
        """
        if not isinstance(expenses, (int, float)):
            raise TypeError("Затраты должны быть типа int или float")
        if expenses < 0:
            raise ValueError("Затраты должны быть положительным числом")
        ...

    def making_a_profit(self, extra_money: float) -> None:
        """
        Получение дополнительных денежных средств.

        :param extra_money: Дополнительные денежные средства

        :return: Количество денежных средств после получения дополнительных денег

        Примеры:
        >>> money = Money(30000, 50000)
        >>> money.making_a_profit(200)
        """
        if not isinstance(extra_money, (int, float)):
            raise TypeError("Дополнительные денежные средства должны быть типа int или float")
        if extra_money < 0:
            raise ValueError("Дополнительные денежные средства должны быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

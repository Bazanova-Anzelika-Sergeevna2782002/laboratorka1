# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class ElectricalNetwork:
    def __init__(self, voltage: float, permissible_voltage: float):
        """
        Создание и подготовка к работе объекта "Электрическая сеть"

        :param voltage: Напряжение
        :param permissible_voltage: Допустимое напряжение

        Примеры:
        >>> electrical_network = ElectricalNetwork(100, 242)  # инициализация экземпляра класса
        """
        if not isinstance(voltage, (int, float)):
            raise TypeError("Напряжение должено быть типа int или float")
        if voltage < 0:
            raise ValueError("Напряжение должен быть неотрицательным числом")
        self.voltage = voltage

        if not isinstance(permissible_voltage, (int, float)):
            raise TypeError("Допустимое напряжение должно быть int или float")
        if permissible_voltage < 0:
            raise ValueError("Допустимое напряжение не может быть отрицательным числом")
        self.permissible_voltage = permissible_voltage

    def an_overloaded_network(self) -> bool:
        """
        Функция которая проверяет является ли электрическая сеть перегруженной

        :return: Является ли электрическая сеть перегруженной

        Примеры:
        >>> electrical_network = ElectricalNetwork(100, 242)
        >>> electrical_network.an_overloaded_network()
        """
        ...

    def voltage_change(self, amendment: float) -> None:
        """
        Изменение напряжения в сети (как в большую, так и в меньшую сторону).
        :param amendment: величина, на которую изменяется напряжение в сети

        :return: Новое напряжение в сети

        Примеры:
        >>> electrical_network = ElectricalNetwork(100, 242)
        >>> electrical_network.voltage_change(10)
        """
        if not isinstance(amendment, (int, float)):
            raise TypeError("величина, на которую изменяется напряжение в сети, должна быть типа int или float")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

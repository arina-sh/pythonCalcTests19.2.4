import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2 # тест сложения

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 2) == 3 # тест вычитания

    def test_division_success(self):
        assert self.calc.division(self, 4, 2) == 2  # тест деления

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4  # тест умножения

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) != 3  # негативный тест сложения

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)  # тест деления на ноль

    def teardown(self):
        print('Выполнение метода Teardown')

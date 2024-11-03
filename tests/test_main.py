import pytest
from src.main import Calculator

class TestCalculator:

    @pytest.mark.parametrize(
        'x, y, res',
        [
            (1, 2, 0.5),
            (5, -1, -5),
            (10, 2, 5),
            (-10, -2, 5),
            (100, 25, 4),
            (50, 0.5, 100),
            (-50, -0.5, 100),
            (1e10, 2, 5e9),           # великі числа
            (1e-10, 2, 5e-11),        # малі числа
            (float('inf'), 2, float('inf')),  # нескінченність
            (1, 0, float('inf')),     # ділення на нуль, може викликати помилку
            (0, 1, 0),
        ]
    )
    def test_divide(self, x, y, res):
        if y == 0:
            with pytest.raises(ZeroDivisionError):
                Calculator().divide(x, y)
        else:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        'x, y, res',
        [
            (1, 2, 3),
            (5, -1, 4),
            (5, 0, 5),
            (0, 5, 5),
            (10, 10, 20),
            (-10, -10, -20),
            (1000, 500, 1500),
            (-1000, -500, -1500),
            (1e10, 2, 1e10 + 2),           # великі числа
            (1e-10, 2, 2 + 1e-10),         # малі числа
            (float('inf'), 1, float('inf')), # нескінченність
            (float('-inf'), 1, float('-inf')), # мінус нескінченність
        ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res

    @pytest.mark.parametrize(
        'x, y, res',
        [
            (3, 2, 1),
            (5, 1, 4),
            (5, 5, 0),
            (10, 3, 7),
            (-5, -5, 0),
            (1000, 100, 900),
            (0, 10, -10),
            (-10, 10, -20),
            (1e10, 2, 1e10 - 2),           # великі числа
            (1e-10, 2, 1e-10 - 2),         # малі числа
            (float('inf'), 1, float('inf') - 1), # нескінченність
            (float('-inf'), 1, float('-inf') - 1), # мінус нескінченність
        ]
    )
    def test_subtract(self, x, y, res):
        assert Calculator().subtract(x, y) == res

    @pytest.mark.parametrize(
        'x, y, res',
        [
            (2, 3, 6),
            (-1, 5, -5),
            (0, 5, 0),
            (4, 4, 16),
            (10, -2, -20),
            (100, 0.01, 1),
            (-100, -10, 1000),
            (5, 5, 25),
            (1e5, 1e5, 1e10),           # великі числа
            (1e-5, 1e5, 1),             # малі числа
            (float('inf'), 1, float('inf')), # нескінченність
            (float('-inf'), 1, float('-inf')), # мінус нескінченність
        ]
    )
    def test_multiply(self, x, y, res):
        assert Calculator().multiply(x, y) == res

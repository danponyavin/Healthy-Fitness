"""
Tests for calculator
"""

import pytest

from ..calculator.calculator_functions import calcUserData, calcIMT


@pytest.mark.parametrize("data, cpfc", [({"gender": 1, "weight": 70, "growth": 177, "age": 18, "activity": 3, "aim": 3},
                                         {'calories': 2935, 'proteins': 257, 'fats': 65, 'carbohydrates': 330}),
                                        ({"gender": 1, "weight": 95, "growth": 180, "age": 25, "activity": 2, "aim": 1},
                                         {'calories': 2419, 'proteins': 242, 'fats': 81, 'carbohydrates': 181}),
                                        ({"gender": 1, "weight": 80, "growth": 193, "age": 37, "activity": 5, "aim": 2},
                                         {'calories': 3470, 'proteins': 260, 'fats': 116, 'carbohydrates': 347}),
                                        ({"gender": 1, "weight": 150, "growth": 200, "age": 45, "activity": 1, "aim": 1},
                                         {'calories': 2732, 'proteins': 273, 'fats': 91, 'carbohydrates': 205}),
                                        ({"gender": 1, "weight": -100, "growth": 15, "age": 10, "activity": 2, "aim": 3},
                                         {'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0}),
                                        ({"gender": 2, "weight": 40, "growth": 155, "age": 16, "activity": 2, "aim": 3},
                                         {'calories': 1706, 'proteins': 149, 'fats': 38, 'carbohydrates': 192}),
                                        ({"gender": 2, "weight": 80, "growth": 170, "age": 23, "activity": 1, "aim": 1},
                                         {'calories': 1713, 'proteins': 171, 'fats': 57, 'carbohydrates': 128}),
                                        ({"gender": 2, "weight": 57, "growth": 169, "age": 18, "activity": 3, "aim": 2},
                                        {'calories': 2132, 'proteins': 160, 'fats': 71, 'carbohydrates': 213}),
                                        ({"gender": 2, "weight": 70, "growth": 200, "age": 30, "activity": 4, "aim": 2},
                                        {'calories': 2827, 'proteins': 212, 'fats': 94, 'carbohydrates': 283}),
                                        ({"gender": 2, "weight": -3, "growth": 0, "age": 5, "activity": 9, "aim": 7},
                                         {'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0})])
def test_calc_user_data(data, cpfc):
    assert calcUserData(data) == cpfc


@pytest.mark.parametrize("growth, weight, imt", [(180, 80, "24.7"),
                                                 (200, 100, "25.0"),
                                                 (0, 100, "Wrong weight or growth"),
                                                 (199, 0, "0.0")])
def test_calc_imt(growth, weight, imt):
    assert calcIMT(growth, weight) == imt

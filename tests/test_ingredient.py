from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:

    @pytest.mark.parametrize('price', [
        45,
        45.99
    ])
    def test_get_price_ingredient(self, price):
        ingredient = Ingredient('SAUCE', 'sauce_1', price)

        assert ingredient.get_price() == price

    def test_get_name_ingredient(self):
        ingredient = Ingredient('SAUCE', 'sauce_1', 45.99)

        assert ingredient.get_name() == 'sauce_1'

    def test_get_type_ingredient(self):
        ingredient = Ingredient('SAUCE', 'sauce_1', 45.99)

        assert ingredient.get_type() == 'SAUCE'

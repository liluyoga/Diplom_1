from praktikum.ingredient import Ingredient
from data import BurgerData
import pytest
import allure


class TestIngredient:

    @allure.title("Проверка получения цены ингредиента int/float")
    @pytest.mark.parametrize('price', [
        45,
        45.99
    ])
    def test_get_price_ingredient(self, price):
        ingredient = Ingredient(BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, price)

        assert ingredient.get_price() == price

    @allure.title("Проверка получения названия ингредиента")
    def test_get_name_ingredient(self):
        ingredient = Ingredient(BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce)

        assert ingredient.get_name() == BurgerData.ingredient_name_sauce

    @allure.title("Проверка получения типа ингредиента")
    def test_get_type_ingredient(self):
        ingredient = Ingredient(BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce)

        assert ingredient.get_type() == BurgerData.ingredient_type_sauce

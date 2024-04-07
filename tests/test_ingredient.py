from praktikum.ingredient import Ingredient
from data import BurgerData
import pytest
import allure


class TestIngredient:

    @allure.title("Проверка получения цены ингредиента int/float")
    @pytest.mark.parametrize('ing_type, ing_name, ing_price', [
        [BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce],
        [BurgerData.ingredient_type_filling, BurgerData.ingredient_name_filling, BurgerData.ingredient_price_filling]
    ])
    def test_get_price_ingredient(self, ing_type, ing_name, ing_price):
        ingredient = Ingredient(ing_type, ing_name, ing_price)

        assert ingredient.get_price() == ing_price

    @allure.title("Проверка получения названия ингредиента")
    @pytest.mark.parametrize('ing_type, ing_name, ing_price', [
        [BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce],
        [BurgerData.ingredient_type_filling, BurgerData.ingredient_name_filling, BurgerData.ingredient_price_filling]
    ])
    def test_get_name_ingredient(self, ing_type, ing_name, ing_price):
        ingredient = Ingredient(ing_type, ing_name, ing_price)

        assert ingredient.get_name() == ing_name

    @allure.title("Проверка получения типа ингредиента")
    @pytest.mark.parametrize('ing_type, ing_name, ing_price', [
        [BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce],
        [BurgerData.ingredient_type_filling, BurgerData.ingredient_name_filling, BurgerData.ingredient_price_filling]
    ])
    def test_get_type_ingredient(self, ing_type, ing_name, ing_price):
        ingredient = Ingredient(ing_type, ing_name, ing_price)

        assert ingredient.get_type() == ing_type

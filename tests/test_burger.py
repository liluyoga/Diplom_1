from praktikum.burger import Burger
from praktikum.database import Database
from data import BurgerData
from unittest.mock import Mock, patch
import pytest
import allure


class TestBurger:

    @allure.title("Проверка установки булочки для бургера")
    def test_set_buns_burger(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name=BurgerData.bun_name, price=BurgerData.bun_price)
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == BurgerData.bun_name and burger.bun.price == BurgerData.bun_price, \
            (f'Название установленной булочки: {burger.bun.name}, цена установленной булочки: {burger.bun.price}.'
             f'Ожидаемое название: {BurgerData.bun_name}, ожидаемая цена: {BurgerData.bun_price}.')

    @allure.title("Проверка добавления ингредиента в бургер")
    def test_add_ingredient_burger(self):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type=BurgerData.ingredient_type_filling, name=BurgerData.ingredient_name_filling, price=BurgerData.ingredient_price_filling)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    @allure.title("Проверка удаления ингредиента из бургера")
    def test_remove_ingredient_burger(self):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type=BurgerData.ingredient_type_filling, name=BurgerData.ingredient_name_filling, price=BurgerData.ingredient_price_filling)
        burger = Burger()
        burger.ingredients.append(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    @allure.title("Проверка перемещения ингредиентов в бургере")
    def test_move_ingredient_burger(self):
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_ingredient_0.configure_mock(ingredient_type=BurgerData.ingredient_type_filling, name=BurgerData.ingredient_name_filling, price=BurgerData.ingredient_price_filling)
        mock_ingredient_1.configure_mock(ingredient_type=BurgerData.ingredient_type_sauce, name=BurgerData.ingredient_name_sauce, price=BurgerData.ingredient_price_sauce)
        burger = Burger()
        burger.ingredients.append(mock_ingredient_0)
        burger.ingredients.append(mock_ingredient_1)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient_1
        assert burger.ingredients[1] == mock_ingredient_0

    @allure.title("Проверка получения стоимости бургера только из булочки int/float")
    @pytest.mark.parametrize('price', [
        300, 330.55
    ])
    def test_get_price_burger_only_bun(self, price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = price
        burger = Burger()
        burger.bun = mock_bun

        expected_result = price * 2
        actual_result = burger.get_price()

        assert actual_result == expected_result

    @allure.title("Проверка получения стоимости бургера из булочки и 2-х ингредиентов int/float")
    @pytest.mark.parametrize("bun_price, ingredient_0_price, ingredient_1_price",
                             [
                                 [300, 800, 100],
                                 [350.55, 800.67, 100.15]
                             ]
                             )
    def test_get_price_burger_with_ingredients(self, bun_price, ingredient_0_price, ingredient_1_price):
        mock_bun = Mock()
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient_0.get_price.return_value = ingredient_0_price
        mock_ingredient_1.get_price.return_value = ingredient_1_price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient_0)
        burger.ingredients.append(mock_ingredient_1)

        expected_result = (bun_price * 2 + ingredient_0_price + ingredient_1_price)
        actual_result = burger.get_price()

        assert actual_result == expected_result

    @allure.title("Проверка получения рецепта бургера только из булочки")
    @patch('praktikum.burger.Burger.get_price', return_value=BurgerData.burger_price_1)
    # замокирован метод get_price из класса Burger, который будет вызываться в методе get_receipt
    def test_get_receipt_burger_only_bun(self, mock_get_price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = BurgerData.bun_name
        burger = Burger()
        burger.bun = mock_bun

        expected_result = '\n'.join([f'(==== {BurgerData.bun_name} ====)', f'(==== {BurgerData.bun_name} ====)\n', f'Price: {BurgerData.burger_price_1}'])
        actual_result = burger.get_receipt()

        assert actual_result == expected_result

    @allure.title("Проверка получения рецепта бургера из булочки и 2-х ингредиентов")
    @patch('praktikum.burger.Burger.get_price', return_value=BurgerData.burger_price_2)
    # замокирован метод get_price из класса Burger, который будет вызываться в методе get_receipt
    def test_get_receipt_burger_with_ingredients(self, mock_get_price):
        mock_bun = Mock()
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_bun.get_name.return_value = BurgerData.bun_name
        mock_ingredient_0.get_type.return_value = BurgerData.ingredient_type_sauce
        mock_ingredient_1.get_type.return_value = BurgerData.ingredient_type_filling
        mock_ingredient_0.get_name.return_value = BurgerData.ingredient_name_sauce
        mock_ingredient_1.get_name.return_value = BurgerData.ingredient_name_filling
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient_0)
        burger.ingredients.append(mock_ingredient_1)

        expected_result = '\n'.join([f'(==== {BurgerData.bun_name} ====)',
                                     f'= {BurgerData.ingredient_type_sauce.lower()} {BurgerData.ingredient_name_sauce} =',
                                     f'= {BurgerData.ingredient_type_filling.lower()} {BurgerData.ingredient_name_filling} =',
                                     f'(==== {BurgerData.bun_name} ====)\n',
                                     f'Price: {BurgerData.burger_price_2}'])
        actual_result = burger.get_receipt()

        assert actual_result == expected_result

    @allure.title("Проверка возможности собрать бургер из данных Database")
    @pytest.mark.parametrize("bun_index, ing_1_index, ing_2_index, expected_price", [
        [0, 0, 3, 400],
        [1, 1, 4, 800],
        [2, 2, 5, 1200]
    ])
    def test_burger_with_database(self, bun_index, ing_1_index, ing_2_index, expected_price):
        burger = Burger()
        database = Database()
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        burger.set_buns(buns[bun_index])
        burger.add_ingredient(ingredients[ing_1_index])
        burger.add_ingredient(ingredients[ing_2_index])

        actual_burger_price = burger.get_price()

        assert actual_burger_price == expected_price

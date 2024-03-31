from praktikum.burger import Burger
from unittest.mock import Mock, patch
import pytest


class TestBurger:

    def test_set_buns_burger(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name='white bun', price=50.50)
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == 'white bun' and burger.bun.price == 50.50

    def test_add_ingredient_burger(self):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type='FILLING', name='Начинка_1', price=300)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_burger(self):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type='FILLING', name='Начинка_1', price=300)
        burger = Burger()
        burger.ingredients.append(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_burger(self):
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_ingredient_0.configure_mock(ingredient_type='FILLING', name='Начинка_1', price=300)
        mock_ingredient_1.configure_mock(ingredient_type='SAUCE', name='Соус_1', price=80)
        burger = Burger()
        burger.ingredients.append(mock_ingredient_0)
        burger.ingredients.append(mock_ingredient_1)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient_1 and burger.ingredients[1] == mock_ingredient_0

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

    @patch('praktikum.burger.Burger.get_price', return_value=2500)
    def test_get_receipt_burger_only_bun(self, mock_get_price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'white bun'
        burger = Burger()
        burger.bun = mock_bun

        expected_result = '\n'.join(['(==== white bun ====)', '(==== white bun ====)\n', 'Price: 2500'])
        actual_result = burger.get_receipt()

        assert actual_result == expected_result

    @patch('praktikum.burger.Burger.get_price', return_value=2500.55)
    def test_get_receipt_burger_with_ingredients(self, mock_get_price):
        mock_bun = Mock()
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_bun.get_name.return_value = 'white bun'
        mock_ingredient_0.get_type.return_value = 'SAUCE'
        mock_ingredient_1.get_type.return_value = 'FILLING'
        mock_ingredient_0.get_name.return_value = 'ingredient_0'
        mock_ingredient_1.get_name.return_value = 'ingredient_1'
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient_0)
        burger.ingredients.append(mock_ingredient_1)

        expected_result = '\n'.join(['(==== white bun ====)', '= sauce ingredient_0 =', '= filling ingredient_1 =', '(==== white bun ====)\n', 'Price: 2500.55'])
        actual_result = burger.get_receipt()

        assert actual_result == expected_result

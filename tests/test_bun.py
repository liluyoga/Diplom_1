from praktikum.bun import Bun
from data import BurgerData
import pytest
import allure


class TestBun:

    @allure.title("Проверка получения названия булочки")
    def test_get_name_bun(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price)

        assert bun.get_name() == BurgerData.bun_name

    @allure.title("Проверка получения цены булочки int/float")
    @pytest.mark.parametrize('price', [
        50,
        50.99
    ])
    def test_get_price_bun(self, price):
        bun = Bun(BurgerData.bun_name, price)

        assert bun.get_price() == price

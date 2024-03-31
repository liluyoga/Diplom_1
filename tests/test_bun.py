from praktikum.bun import Bun
import pytest


class TestBun:

    def test_get_name_bun(self):
        bun = Bun('white bun', 50.50)

        assert bun.get_name() == 'white bun'

    @pytest.mark.parametrize('price', [
        50,
        50.99
    ])
    def test_get_price_bun(self, price):
        bun = Bun('white bun', price)

        assert bun.get_price() == price

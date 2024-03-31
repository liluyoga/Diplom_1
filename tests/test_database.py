import pytest

from praktikum.database import Database
from unittest.mock import Mock


class TestDatabase:

    def test_available_buns_no_buns(self):
        database = Database()
        actual_result = database.available_buns()

        assert actual_result == database.buns

    def test_available_buns_one_bun(self):
        mock_bun = Mock()
        database = Database()
        database.buns.append(mock_bun)

        actual_result = database.available_buns()

        assert actual_result == database.buns

    def test_available_buns_few_buns(self):
        mock_bun_0 = Mock()
        mock_bun_1 = Mock()
        mock_buns = [mock_bun_0, mock_bun_1]
        database = Database()
        for item in mock_buns:
            database.buns.append(item)

        actual_result = database.available_buns()

        assert actual_result == database.buns

    def test_available_ingredients_no_ingredients(self):
        database = Database()
        actual_result = database.available_ingredients()

        assert actual_result == database.ingredients

    def test_available_ingredients_one_ingredient(self):
        mock_ingredient = Mock()
        database = Database()
        database.ingredients.append(mock_ingredient)

        actual_result = database.available_ingredients()

        assert actual_result == database.ingredients

    def test_available_ingredients_few_ingredients(self):
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_ingredients = [mock_ingredient_0, mock_ingredient_1]
        database = Database()
        for item in mock_ingredients:
            database.ingredients.append(item)

        actual_result = database.available_ingredients()

        assert actual_result == database.ingredients
import unittest
from ..recipe import Recipe, Ingredient
from ..fermentable import Fermentable


class TestRecipe(unittest.TestCase):

    def setUp(self):

        ingredients = [
            Ingredient(Fermentable(0.781), 2, None)
            ]

        self.recipe = Recipe(10, None, ingredients)

    def test_degrees_plato(self):

        """ """

        self.assertEquals(self.recipe.degrees_plato, 0)

    def test_SG(self):

        """ """

        self.assertEquals(self.recipe.SG, 0)


if __name__ == '__main__':

    unittest.main()
